# EJERCICIO 12 - DENNIS ALFREDO ROMERO ROJAS
# Pseudocódigo:
# PASO 01: Solicitar al usuario ingresar el nombre del archivo

nombre_archivo = input("Ingrese el nombre del archivo: ")

# PASO 02: Obtener la extensión del archivo
extension = nombre_archivo.split('.')[-1].lower()

# PASO 03: Definir el diccionario de tipos MIME
# Se ha tomado como referencia el enlace enviado en el ejercicio: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
tipos_mime = {

    'aac': 'audio/aac',
    'abw': 'application/x-abiword',
    'arc': 'application/x-freearc',
    'avi': 'video/x-msvideo',
    'azw': 'application/vnd.amazon.ebook',
    'bin': 'application/octet-stream',
    'bmp': 'image/bmp',
    'bz': 'application/x-bzip',
    'bz2': 'application/x-bzip2',
    'csh': 'application/x-csh',
    'css': 'text/css',
    'csv': 'text/csv',
    'doc': 'application/msword',
    'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'eot': 'application/vnd.ms-fontobject',
    'epub': 'application/epub+zip',
    'gz': 'application/gzip',
    'gif': 'image/gif',
    'htm': 'text/html',
    'html': 'text/html',
    'ico': 'image/vnd.microsoft.icon',
    'ics': 'text/calendar',
    'jar': 'application/java-archive',
    'jpeg': 'image/jpeg',
    'jpg': 'image/jpeg',
    'js': 'application/javascript',
    'json': 'application/json',
    'jsonld': 'application/ld+json',
    'mid': 'audio/midi audio/x-midi',
    'midi': 'audio/midi audio/x-midi',
    'mjs': 'text/javascript',
    'mp3': 'audio/mpeg',
    'mp4': 'video/mp4',
    'mpeg': 'video/mpeg',
    'mpkg': 'application/vnd.apple.installer+xml',
    'odp': 'application/vnd.oasis.opendocument.presentation',
    'ods': 'application/vnd.oasis.opendocument.spreadsheet',
    'odt': 'application/vnd.oasis.opendocument.text',
    'oga': 'audio/ogg',
    'ogv': 'video/ogg',
    'ogx': 'application/ogg',
    'otf': 'font/otf',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'ppt': 'application/vnd.ms-powerpoint',
    'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'rar': 'application/vnd.rar',
    'rtf': 'application/rtf',
    'sh': 'application/x-sh',
    'svg': 'image/svg+xml',
    'swf': 'application/x-shockwave-flash',
    'tar': 'application/x-tar',
    'tif': 'image/tiff',
    'tiff': 'image/tiff',
    'ts': 'video/mp2t',
    'ttf': 'font/ttf',
    'txt': 'text/plain',
    'vsd': 'application/vnd.visio',
    'wav': 'audio/wav',
    'weba': 'audio/webm',
    'webm': 'video/webm',
    'webp': 'image/webp',
    'woff': 'font/woff',
    'woff2': 'font/woff2',
    'xhtml': 'application/xhtml+xml',
    'xls': 'application/vnd.ms-excel',
    'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'xml': 'application/xml',
    'xul': 'application/vnd.mozilla.xul+xml',
    'zip': 'application/zip',
    '3gp': 'video/3gpp',
    '3g2': 'video/3gpp2',
    '7z': 'application/x-7z-compressed'
}
# PASO 04: En función al paso anterior, se procederá a obtener el tipo MIME correspondiente
tipo_mime = tipos_mime.get(extension, 'application/octet-stream')

# PASO 05: Mostrar el resultado en consola, precisando el tipo MIME del archivo
print("Tipo MIME del archivo {}: {}".format(nombre_archivo, tipo_mime))
