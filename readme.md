# Tmdb-App

**Tmdb-App** es una aplicación de línea de comandos para explorar información sobre películas utilizando la API de TMDB. Puedes buscar películas populares, en cartelera, mejor valoradas y próximas a estrenarse.

### **Requisitos**

Para ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install -r requirements.txt
```

### **Cómo ejecutar la aplicación**

Para ejecutar la aplicación, usa el siguiente comando:

```bash
python3 main.py movies --type <tipo>
```

Los tipos de películas que puedes buscar son:

- `popular`: Películas populares.
- `playing`: Películas en cartelera.
- `top`: Películas mejor valoradas.
- `upcoming`: Próximos estrenos.

### **Ejemplos de Uso**

1. **Buscar películas populares:**

   ```bash
   python3 main.py movies --type popular
   ```

   Este comando muestra una lista de las películas más populares actualmente.

2. **Buscar películas en cartelera:**

   ```bash
   python3 main.py movies --type playing
   ```

   Este comando muestra una lista de las películas que actualmente están en cartelera.

3. **Buscar películas mejor valoradas:**

   ```bash
   python3 main.py movies --type top
   ```

   Este comando muestra una lista de las películas mejor valoradas.

4. **Buscar próximos estrenos:**

   ```bash
   python3 main.py movies --type upcoming
   ```

   Este comando muestra una lista de las películas próximas a estrenarse.

### **Dependencias**

- **Typer**: Para la creación de la interfaz de línea de comandos.
- **Requests**: Para realizar solicitudes HTTP a la API de TMDB.
- **Otros**: Asegúrate de revisar `requirements.txt` para otras dependencias necesarias.

### **Contacto**

Si tienes alguna duda o sugerencia, no dudes en contactar con el equipo de desarrollo por [jaracalle2041@gmail.com](jaracalle2041@gmail.com), proyecto desarrollado para [Roadmap.sh](https://roadmap.sh/projects/tmdb-cli)