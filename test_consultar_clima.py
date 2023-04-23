import subprocess

def test_python_command_execution():
    result = subprocess.run(["python", "consultar_clima.py"], capture_output=True, text=True)
    exit_code = result.returncode
    
    # Verifica que el código de salida sea 0
    assert exit_code == 0, f"El código de salida fue {exit_code}. Se esperaba 0."
