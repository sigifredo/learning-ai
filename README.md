# Introducción a Deep Learning

Configurar mi entorno virtual:

```console
python3 -m venv venv
source venv/bin/activate
pip install -U numpy matplotlib keras tensorflow[and-cuda]
```

## Configurar backend de Keras

Para configurar el backend con Tensorflow, debemos abrir el archivo `~/.keras/keras.json`, y agregar:

```json
{
    "backend": "tensorflow",
    "epsilon": 1e-7,
    "floatx": "float32",
    "image_data_format": "channels_last"
}
```

## Obtener el directorio de caché de pip

```console
pip cache info
```

## Compilar Python

```console
pip install nuitka
nuitka --standalone --onefile --lto script.py
```
