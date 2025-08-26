from django.shortcuts import render, redirect

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

from django.contrib import messages

from .models import Contacto

import os

import subprocess

import requests

def home(request):
    return render(request, 'bookspace_app/home.html')

def empresa(request):
    return render(request, 'bookspace_app/empresa.html')

def productos(request):
    return render(request, 'bookspace_app/productos.html')

def oferta_del_mes(request):
    return render(request, 'bookspace_app/oferta_del_mes.html')

def localizacion(request):
    return render(request, 'bookspace_app/localizacion.html')

def contacto(request):
    return render(request, 'bookspace_app/contacto.html')

def noticias(request):
    return render(request, 'bookspace_app/noticias.html')

def clima(request):
    return render(request, 'bookspace_app/clima.html')

def login_view(request):
    return render(request, 'bookspace_app/login.html')


# Nueva vista para obtener el clima desde la API
def obtener_clima(request):
    ciudad = request.GET.get("ciudad", "")
    if not ciudad:
        return JsonResponse({"error": "No se proporcionó ciudad"}, status=400)

    api_key = settings.OWM_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return JsonResponse({"error": f"Error de API: {response.status_code}"}, status=response.status_code)

        data = response.json()

        datos = {
            "success": True,
            "ciudad": data["name"],
            "pais": data["sys"]["country"],
            "temperatura": round(data["main"]["temp"], 1),
            "humedad": data["main"]["humidity"],
            "descripcion": data["weather"][0]["description"],
            "viento": data["wind"]["speed"],
        }

        return JsonResponse(datos)

    except Exception as e:
        return JsonResponse({"error": f"Error obteniendo clima: {str(e)}"}, status=500)


def productos(request):
    libros = [
        {'titulo': 'Little Black Book', 'autor': 'Otegha Uwagba', 'precio': 17.29, 'imagen': 'bookspace_app/img/libro1.jpg'},
        {'titulo': 'Your Soul is a River', 'autor': 'Nikita Gill', 'precio': 22.05, 'imagen': 'bookspace_app/img/libro2.jpg'},
        {'titulo': 'The Strength in our Scars', 'autor': 'Bianca Sparacino', 'precio': 11.42, 'imagen': 'bookspace_app/img/libro3.jpg'},
        {'titulo': 'The Polaroid Book', 'autor': 'Barbara Hitchcock', 'precio': 21.30, 'imagen': 'bookspace_app/img/libro4.jpg'},
        {'titulo': 'Python for Unix and Linux', 'autor': 'Jeremy M. Jones y Noah Gift', 'precio': 26.70, 'imagen': 'bookspace_app/img/libro5.jpg'},
        {'titulo': 'Harry Potter und der Stein der Weisen', 'autor': 'Joanne K. Rowling', 'precio': 27.99, 'imagen': 'bookspace_app/img/libro6.jpg', 'extra_class': 'izq'},
        {'titulo': 'Hygge', 'autor': 'Meik Wiking', 'precio': 18.07, 'imagen': 'bookspace_app/img/libro7.jpg'},
        {'titulo': "This is for The Women Who Don't Give a Fuck", 'autor': 'Janne Robinson', 'precio': 21.48, 'imagen': 'bookspace_app/img/libro8.jpg'},
        {'titulo': 'Piensa como un Artista', 'autor': 'Will Gompertz', 'precio': 16.12, 'imagen': 'bookspace_app/img/libro9.jpg'},
        {'titulo': 'Vestules Naktssargam', 'autor': 'Sandra Vensko', 'precio': 11.28, 'imagen': 'bookspace_app/img/libro10.jpg'},
        {'titulo': 'Where Are You?', 'autor': 'Nikita Tzortzis', 'precio': 23.30, 'imagen': 'bookspace_app/img/libro11.jpg'},
        {'titulo': 'Graphic Design', 'autor': 'Jens Muller', 'precio': 18.55, 'imagen': 'bookspace_app/img/libro12.jpg'},
        {'titulo': 'The Sun and Her Flowers', 'autor': 'Rupi Kaur', 'precio': 13.33, 'imagen': 'bookspace_app/img/libro13.jpg'},
        {'titulo': 'Take the Risk', 'autor': 'Ben Carson', 'precio': 14.99, 'imagen': 'bookspace_app/img/nuevo_libro.jpg'},
        {'titulo': "The Passion Within: A Woman's Journal", 'autor': 'Promise Journals', 'precio': 16.50, 'imagen': 'bookspace_app/img/nuevo_libro2.jpg'},
        {'titulo': 'The World Atlas of Coffee', 'autor': 'James Hoffman', 'precio': 12.39, 'imagen': 'bookspace_app/img/nuevo_libro3.jpg'},
    ]
    return render(request, 'bookspace_app/productos.html', {'libros': libros})


def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        email = request.POST.get("email", "").strip()
        mensaje = request.POST.get("mensaje", "").strip()

        # Validaciones
        if not nombre or not email or not mensaje:
            messages.error(request, "Por favor completa todos los campos.")
            return redirect("contacto")

        # Validar email
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Email inválido.")
            return redirect("contacto")

        # Guardar en base de datos
        contacto = Contacto.objects.create(
            nombre=nombre,
            email=email,
            mensaje=mensaje
        )

        messages.success(request, "¡Mensaje enviado exitosamente!")

        # Crear CSV temporal
        csv_filename = f"contacto_{contacto.id}_{contacto.fecha_creacion.strftime('%Y-%m-%d_%H-%M-%S')}.csv"
        temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp")
        os.makedirs(temp_dir, exist_ok=True)
        csv_path = os.path.join(temp_dir, csv_filename)

        import csv
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Nombre", "Email", "Mensaje", "Fecha"])
            writer.writerow([contacto.id, nombre, email, mensaje, contacto.fecha_creacion])

        # Llamar script FTP
        ftp_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts", "ftp.py")
        try:
            result = subprocess.run(
                ["python3", ftp_script, csv_path, csv_filename],
                capture_output=True,
                text=True,
                check=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Error FTP:", e.stderr)

        # Eliminar archivo temporal
        if os.path.exists(csv_path):
            os.remove(csv_path)

        return redirect("contacto")

    return render(request, "bookspace_app/contacto.html")

