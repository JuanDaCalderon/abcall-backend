from datetime import datetime
from typing import List
from sqlalchemy.orm import Session


def generar_respuesta(descripcion):
        desc = descripcion.lower().strip() 
        palabras = desc.split() 
        if '1' in palabras:
            return '''Por favor, intenta lo siguiente para resolver el problema de conexión: 
        1) Revisa que tu dispositivo esté conectado a internet; 
        2) Reinicia tu router o punto de acceso; 
        3) Verifica que no haya restricciones de red en tu firewall o antivirus. Si el problema persiste, contáctanos para mayor asistencia.
        
        ¿Tu solicitud fue resuelta?
        Por favor escribe "si" o "no".'''
        
        elif '2' in palabras:
            return '''Sigue estos pasos para resolver problemas de inicio de sesión: 
        1) Verifica que tu nombre de usuario y contraseña sean correctos; 
        2) Intenta restablecer tu contraseña si la olvidaste; 
        3) Limpia el caché de tu navegador o usa el modo incógnito. Si aún tienes problemas, no dudes en contactarnos.
        
        ¿Tu solicitud fue resuelta?
        Por favor escribe "si" o "no".'''
        
        elif '3' in palabras:
            return '''Si la aplicación está lenta, intenta lo siguiente: 
        1) Cierra las aplicaciones en segundo plano para liberar memoria; 
        2) Limpia el caché de la aplicación; 
        3) Reinicia tu dispositivo. Si el problema persiste, podría ser necesario actualizar la aplicación o contactar a soporte.
        
        ¿Tu solicitud fue resuelta?
        Por favor escribe "si" o "no".'''
        
        elif '4' in palabras:
            return '''Para actualizar a la última versión: 
        1) Ve a la tienda de aplicaciones (App Store o Google Play) y busca nuestra aplicación; 
        2) Presiona "Actualizar" si está disponible. Asegúrate de estar conectado a Wi-Fi y de tener suficiente espacio en el dispositivo. Si encuentras problemas durante la actualización, contáctanos.
        
        ¿Tu solicitud fue resuelta?
        Por favor escribe "si" o "no".'''
        
        elif '5' in palabras:
            return '''Si ves una pantalla en blanco o la aplicación no carga, intenta: 
        1) Cerrar y volver a abrir la aplicación; 
        2) Reiniciar tu dispositivo; 
        3) Verificar que tienes la última versión instalada. Si el problema continúa, es posible que tengamos una interrupción temporal del servicio.
        
        ¿Tu solicitud fue resuelta?
        Por favor escribe "si" o "no".'''
        
        elif '6' in palabras:
            return '''Para procesar un reembolso, sigue estos pasos: 
        1) Completa el formulario de solicitud de devolución en nuestra plataforma; 
        2) Adjunta cualquier documentación necesaria, como el comprobante de pago; 
        3) Envía la solicitud y espera la confirmación. Si tienes dudas, nuestro equipo de soporte está aquí para ayudarte.
        ¿Tu solicitud fue resuelta?
        Por favor escribe "si" o "no".'''
        
        elif '7' in palabras:
            return '''Para resolver problemas de facturación, por favor: 
        1) Revisa el historial de pagos en tu cuenta; 
        2) Confirma que el método de pago sea válido y esté actualizado; 
        3) Si ves cargos desconocidos, contáctanos con los detalles para investigar y asistirte.
        
        ¿Tu solicitud fue resuelta?
        Por favor escribe "si" o "no".'''
        
        elif '8' in palabras:
            return '''Para solucionar problemas de instalación: 
        1) Asegúrate de que tu dispositivo cumple con los requisitos mínimos del sistema; 
        2) Verifica que tengas suficiente espacio de almacenamiento; 
        3) Reinicia tu dispositivo y vuelve a intentar la instalación. Si el error persiste, contacta a soporte técnico.
        ¿Tu solicitud fue resuelta?
        Por favor escribe "si" o "no".'''
        
        elif '9' in palabras:
            return '''Si no recibes notificaciones, intenta: 
        1) Revisar que las notificaciones estén habilitadas en la configuración de la aplicación y del dispositivo; 
        2) Asegúrate de que el dispositivo no esté en modo "No molestar"; 
        3) Reiniciar la aplicación. Contáctanos si necesitas ayuda adicional.
        ¿Tu solicitud fue resuelta?
        Por favor escribe "si" o "no".'''
        
        elif '10' in palabras:
            return '''Si tienes problemas con permisos, sigue estos pasos: 
        1) Ve a "Configuración" en tu dispositivo y selecciona nuestra aplicación; 
        2) Asegúrate de que los permisos necesarios estén activados (como cámara, almacenamiento, etc.); 
        3) Si el problema persiste, intenta reinstalar la aplicación para reestablecer los permisos.
        
        ¿Tu solicitud fue resuelta?
        Por favor escribe "si" o "no".'''
        
        elif 'si' in palabras:
            return '''Gracias por contactarnos. Que tengas un buen día.'''
        elif 'no' in palabras: 
            return '''Hola, gracias por comunicarte con nosotros.
                    Por favor escribe el número que representa la opción de tu consulta de acuerdo con lo siguiente:
                    1. Error de conexión
                    2. Problema de login
                    3. Aplicación lenta
                    4. Actualización
                    5. Pantalla en blanco
                    6. Reembolso
                    7. Facturación
                    8. No puedo instalar
                    9. No recibe
                    10. Permiso'''
        else:
            return '''Hola, gracias por comunicarte con nosotros.
                    Por favor escribe el número que representa la opción de tu consulta de acuerdo con lo siguiente:
                    1. Error de conexión
                    2. Problema de login
                    3. Aplicación lenta
                    4. Actualización
                    5. Pantalla en blanco
                    6. Reembolso
                    7. Facturación
                    8. No puedo instalar
                    9. No recibe
                    10. Permiso'''

