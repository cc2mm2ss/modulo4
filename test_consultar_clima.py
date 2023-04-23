import subprocess

def test_python_command_execution():
    # Ejecuta el comando de Python y obtiene el código de salida y la salida estándar
    result = subprocess.run(["python", "consultar_clima.py"], capture_output=True, text=True)
    exit_code = result.returncode
    stdout = result.stdout

    # Verifica que el código de salida sea 0
    assert exit_code == 0, f"El código de salida fue {exit_code}. Se esperaba 0."

    # Verifica que tres líneas distintas tengan valores diferentes a nulo o cero
    lines = stdout.split("\n")
    assert len(lines) >= 4, "La salida de la aplicación debe tener al menos tres líneas"

    # Verifica que la primera, segunda y tercera línea tengan valores distintos a nulo o cero
    assert lines[0], "La primera línea no debe estar vacía"
    assert lines[1], "La segunda línea no debe estar vacía"
    assert lines[2], "La tercera línea no debe estar vacía"
    assert lines[3], "La tercera línea no debe estar vacía"
