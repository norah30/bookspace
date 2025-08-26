// Función principal para obtener clima
function obtenerClima() {
  const ciudadInput = document.getElementById("ciudad");
  const ciudad = ciudadInput.value.trim();

  console.log("Iniciando búsqueda para:", ciudad);

  // Validar entrada
  if (!ciudad) {
    mostrarError("Por favor ingresa el nombre de una ciudad");
    return;
  }

  // Mostrar estado de carga
  mostrarLoading();

  const url = `/obtener-clima/?ciudad=${encodeURIComponent(ciudad)}`;

  console.log(" URL de petición:", url);

  //peticion manejo de errores
  fetch(url, {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      console.log("Respuesta recibida:", response.status);

      if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`);
      }

      return response.text();
    })
    .then((text) => {
      console.log("Respuesta cruda:", text);

      // Intentar parsear JSON
      try {
        const datos = JSON.parse(text);
        console.log("Datos parseados:", datos);

        if (datos.error) {
          mostrarError(datos.error);
        } else if (datos.success) {
          mostrarClima(datos);
        } else {
          mostrarError("Respuesta inesperada del servidor");
        }
      } catch (e) {
        console.error("Error parseando JSON:", e);
        mostrarError(
          "Error en la respuesta del servidor: " + text.substring(0, 100)
        );
      }
    })
    .catch((error) => {
      console.error("Error en fetch:", error);
      mostrarError("Error al conectar con el servidor: " + error.message);
    })
    .finally(() => {
      ocultarLoading();
    });
}

// Mostrar datos del clima
function mostrarClima(datos) {
  console.log(" Mostrando datos del clima:", datos);

  // Actualizar temperatura
  const tempElement = document.getElementById("temp-actual");
  if (tempElement) {
    tempElement.textContent = `${datos.temperatura}°C`;
  }

  // Actualizar detalles
  const humedadElement = document.getElementById("humedad");
  if (humedadElement) {
    humedadElement.textContent = `Humedad: ${datos.humedad}%`;
  }

  const descripcionElement = document.getElementById("descripcion");
  if (descripcionElement) {
    descripcionElement.textContent = datos.descripcion;
  }

  const vientoElement = document.getElementById("viento");
  if (vientoElement) {
    vientoElement.textContent = `Viento: ${datos.viento} km/h`;
  }

  // Actualizar título con ciudad
  const titulo = document.querySelector(".clima h1");
  if (titulo) {
    titulo.textContent = `Clima en ${datos.ciudad}${
      datos.pais ? ", " + datos.pais : ""
    }`;
  }

  // Limpiar errores previos
  limpiarError();

  // Mostrar datos
  const datosClimaElement = document.getElementById("datos-clima");
  if (datosClimaElement) {
    datosClimaElement.style.display = "block";
  }

  console.log("Datos del clima mostrados correctamente");
}

// Mostrar error
function mostrarError(mensaje) {
  console.log(" Mostrando error:", mensaje);
  limpiarError();

  const errorDiv = document.createElement("div");
  errorDiv.className = "mensaje-error";
  errorDiv.innerHTML = `<strong>Error:</strong> ${mensaje}`;

  const climaSection = document.querySelector(".clima");
  const datosClima = document.getElementById("datos-clima");

  if (climaSection && datosClima) {
    climaSection.insertBefore(errorDiv, datosClima);
  }

  // Ocultar datos del clima
  if (datosClima) {
    datosClima.style.display = "none";
  }
}

// Limpiar errores
function limpiarError() {
  const errorExistente = document.querySelector(".mensaje-error");
  if (errorExistente) {
    errorExistente.remove();
  }
}

// Mostrar loading
function mostrarLoading() {
  const button = document.querySelector(".busqueda-ciudad button");
  if (button) {
    button.disabled = true;
    button.textContent = "Buscando...";
  }
}

// Ocultar loading
function ocultarLoading() {
  const button = document.querySelector(".busqueda-ciudad button");
  if (button) {
    button.disabled = false;
    button.textContent = "Buscar Clima";
  }
}

// Permitir buscar con Enter
document.addEventListener("DOMContentLoaded", function () {
  console.log("JavaScript de clima cargado");

  const ciudadInput = document.getElementById("ciudad");
  if (ciudadInput) {
    ciudadInput.addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        obtenerClima();
      }
    });
  }
});

// Función de prueba para debug
function probarConexion() {
  console.log("Probando conexión directa...");
  const url = "/obtener-clima/?ciudad=Madrid";

  fetch(url)
    .then((response) => response.text())
    .then((text) => {
      console.log(" Respuesta de prueba:", text);
    })
    .catch((error) => {
      console.error("Error en prueba:", error);
    });
}
