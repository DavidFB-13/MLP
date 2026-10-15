# Entorno Python

Esta carpeta tiene un entorno virtual `.venv` creado con Python 3.14.6.
Incluye NumPy para cálculos y Matplotlib para gráficos. Las versiones instaladas
están guardadas en `requirements.txt`.
VS Code está configurado para usarlo. Abre la carpeta MLP completa.
Si VS Code conserva otro intérprete, ejecuta **Python: Select Interpreter**
y selecciona `.venv\Scripts\python.exe`.

## Uso en PowerShell

Activar el entorno en una terminal nueva:

```powershell
.\.venv\Scripts\Activate.ps1
python main.py
python -m pip install nombre_del_paquete
```

También puedes usarlo sin activación:

```powershell
.\.venv\Scripts\python.exe main.py
.\.venv\Scripts\python.exe -m pip install nombre_del_paquete
```

En VS Code puedes ejecutar con **Run Python File** y depurar con **F5**.
`main.py` está vacío: no mostrará nada hasta que escribas código.

## Recrear el entorno

Si mueves la carpeta a otro ordenador, crea de nuevo `.venv`:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Instala las bibliotecas que necesite tu programa dentro de este entorno.
El entorno virtual no se debe compartir ni guardar en Git.

## Git, GitHub y GitLens

Git guarda versiones del proyecto en este ordenador. Cada **commit** es una
versión guardada con un mensaje. GitHub aloja una copia del repositorio en línea.
GitLens permite explorar el historial y los cambios desde VS Code.

Para publicar por primera vez, abre MLP en VS Code, pulsa `Ctrl+Shift+P` y
ejecuta **Publish to GitHub**. Inicia sesión en el navegador si se solicita
y elige la visibilidad del repositorio.

Para guardar cambios posteriores:

1. Abre **Control de código fuente** con `Ctrl+Shift+G`.
2. Revisa los cambios y pulsa `+` en los archivos que quieras incluir.
3. Escribe un mensaje descriptivo y pulsa **Commit**.
4. Pulsa **Sincronizar cambios** para enviarlos a GitHub y recibir cambios remotos.

Un commit se guarda localmente; el envío a GitHub se llama **push**.
`.venv`, las cachés de Python y `.env` están excluidos mediante `.gitignore`.

Para explorar versiones anteriores, busca **GitLens: Show Commit Graph** en
la paleta de comandos. La conexión adicional con GitHub se configura mediante
**GitLens: Manage Integrations**; completa la autorización en el navegador
si quieres usar las funciones de esa integración.
