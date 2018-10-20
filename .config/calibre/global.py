# calibre wide preferences

### Begin group: DEFAULT
 
# database path
# Путь к базе данных в которой хранятся книги
database_path = '/home/djaler/library1.db'
 
# filename pattern
# Шаблон для получения метаданных из имени файла
filename_pattern = u'(?P<title>.+) - (?P<author>[^_]+)'
 
# isbndb com key
# Ключ доступа к isbndb.com
isbndb_com_key = ''
 
# network timeout
# Таймаут для сетевых операций по умолчанию (сек)
network_timeout = 5
 
# library path
# Путь к директории в которой хранятся книги
library_path = u'/home/djaler/Stuff/Books'
 
# language
# Язык для отображения пользовательского интерфейса
language = 'ru'
 
# output format
# Умолчальный формат вывода для преобразования электронных книг.
output_format = u'epub'
 
# input format order
# Упорядоченный список предпочитаемых форматов
input_format_order = cPickle.loads('\x80\x02]q\x01(X\x03\x00\x00\x00PDFq\x02X\x04\x00\x00\x00EPUBq\x03X\x04\x00\x00\x00AZW3q\x04X\x04\x00\x00\x00MOBIq\x05X\x03\x00\x00\x00LITq\x06X\x03\x00\x00\x00PRCq\x07X\x03\x00\x00\x00FB2q\x08X\x04\x00\x00\x00HTMLq\tX\x03\x00\x00\x00HTMq\nX\x04\x00\x00\x00XHTMq\x0bX\x05\x00\x00\x00SHTMLq\x0cX\x05\x00\x00\x00XHTMLq\rX\x03\x00\x00\x00ZIPq\x0eX\x04\x00\x00\x00DOCXq\x0fX\x03\x00\x00\x00ODTq\x10X\x03\x00\x00\x00RTFq\x11X\x03\x00\x00\x00TXTq\x12X\x04\x00\x00\x00TEXTq\x13X\x06\x00\x00\x00RECIPEq\x14X\x04\x00\x00\x00DJVUq\x15X\x03\x00\x00\x00AZWq\x16X\x03\x00\x00\x00CBCq\x17X\x04\x00\x00\x00AZW4q\x18X\x04\x00\x00\x00PMLZq\x19X\x04\x00\x00\x00POBIq\x1aX\x03\x00\x00\x00RARq\x1bX\x02\x00\x00\x00RBq\x1cX\x03\x00\x00\x00PMLq\x1dX\x05\x00\x00\x00HTMLZq\x1eX\x08\x00\x00\x00MARKDOWNq\x1fX\x03\x00\x00\x00DJVq X\x11\x00\x00\x00DOWNLOADED_RECIPEq!X\x03\x00\x00\x00CHMq"X\x03\x00\x00\x00TCRq#X\x04\x00\x00\x00DOCMq$X\x04\x00\x00\x00SHTMq%X\x04\x00\x00\x00UPDBq&X\x02\x00\x00\x00MDq\'X\x03\x00\x00\x00SNBq(X\x03\x00\x00\x00LRFq)X\x03\x00\x00\x00CBRq*X\x03\x00\x00\x00OPFq+X\x04\x00\x00\x00TXTZq,X\x03\x00\x00\x00CBZq-X\x03\x00\x00\x00PDBq.X\x07\x00\x00\x00TEXTILEq/e.')
 
# read file metadata
# Читать метаданные из файлов
read_file_metadata = True
 
# worker process priority
# Приоритет работы процесса. Более высокий приоритет означает более быструю работу и более высокое потребление ресурсов. Большинство задач вроде конвертации/новых загрузок/добавления книг/и т.д. зависят от этого параметра.
worker_process_priority = 'normal'
 
# swap author names
# Поменять местами имя и фамилию автора при чтении метаданных
swap_author_names = False
 
# add formats to existing
# Добавить новые форматы к существующим записям книг
add_formats_to_existing = False
 
# check for dupes on ctl
# Проверьте на наличие дубликатов перед копированием в другую библиотеку
check_for_dupes_on_ctl = False
 
# installation uuid
# Installation UUID
installation_uuid = '01f18a9e-b50e-466f-940b-f43badbdcd99'
 
# new book tags
# Теги, добавляемые к книгам в библиотеке
new_book_tags = cPickle.loads('\x80\x02]q\x01.')
 
# mark new books
# Пометить недавно добавленные книги. Отметки временные и автоматически удаляются после перезагрузки calibre.
mark_new_books = False
 
# saved searches
# Список сохраненных поисковых запросов
saved_searches = cPickle.loads('\x80\x02}q\x01.')
 
# user categories
# Пользовательские категории в браузере тегов
user_categories = cPickle.loads('\x80\x02}q\x01.')
 
# manage device metadata
# Как и когда calibre обновляет метаданные на устройстве.
manage_device_metadata = u'on_connect'
 
# limit search columns
# При поиске в тексте без использования поисковых префиксов, например, Red (красный) вместо title:Red (название:красный), ограничить столбцы поиска указанными ниже.
limit_search_columns = False
 
# limit search columns to
# Выберите столбцы для поиска, когда не используется префикс, например Red вместо title:Red. Введите список названий поиска разделённых запятой. Будет полезно только если вы установите ограничение столбцов поиска выше.
limit_search_columns_to = cPickle.loads('\x80\x02]q\x01(U\x05titleq\x02U\x07authorsq\x03U\x04tagsq\x04U\x06seriesq\x05U\tpublisherq\x06e.')
 
# use primary find in search
# Символы, набранные в поисковой строке будут соответствовать их акцентированным версиям, основываясь на выбранном для интерфейса Calibre языке. Для примера, на английском, поиску для n будет соответствовать ñ и n, но если ваш язык - Испанский, ему будет соответствовать только n. Заметьте, что это гораздо медленнее, чем простой поиск в очень больших библиотеках. Также учтите, что эта опция не будет работать, если вы включили регистрозависимый поиск.
use_primary_find_in_search = True
 
# case sensitive
# Сделать поиск регистрозависимым
case_sensitive = False
 
# migrated
# For Internal use. Don't modify.
migrated = False
 


