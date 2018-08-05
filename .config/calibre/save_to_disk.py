# Опции для  управления сохранением на диск

### Begin group: DEFAULT
 
# update metadata
# По умолчанию calibre обновляет метаданные в сохранённых файлах в библиотеке. Может замедлить запись на диск.
update_metadata = True
 
# write opf
# Обычно, calibre будет писать метаданные в отдельный файл OPF рядом с файлом электронной книги.
write_opf = False
 
# save cover
# Обычно, calibre будет сохранять обложку в отдельном файле рядом с файлами электронной книги.
save_cover = False
 
# formats
# Список форматов, разделенных запятыми, для сохранения для каждой книги. По умолчанию все доступные форматы сохраняются.
formats = 'all'
 
# template
# Шаблон для управления названием файла и структурой папки с сохранёнными файлами. По умолчанию "{author_sort}/{title}/{title} - {authors}" будет сохранять книги в подпапку с именем автора и названиями файлов включающими название и автора. Доступные настройки: {author_sort, authors, id, isbn, languages, last_modified, pubdate, publisher, rating, series, series_index, tags, timestamp, title}
template = u'{author_sort}/{title}/{title} - {authors}'
 
# send template
# Шаблон для управления названием файла и структурой папки с файлами, отправляемыми на устройство. По умолчанию "{author_sort}/{title} - {authors}" будет сохранять книги в подпапку с именем автора и названиями файлов, включающими название и автора. Доступные настройки: {publisher, series_index, isbn, pubdate, rating, series, author_sort, languages, authors, last_modified, timestamp, title, id, tags}
send_template = u'{author_sort}/{title} - {authors}'
 
# asciiize
# По умолчанию, в именах файлов calibre конвертирует все не английские символы в английские эквиваленты. ПРЕДУПРЕЖДЕНИЕ: если вы выключите эту опцию, могут появиться ошибки при сохранении, в зависимости от того, насколько хорошо поддерживает юникод файловая система, в которой вы сохраняете.
asciiize = False
 
# timefmt
# Формат отображения дат.  %d - день, %b - месяц, %m - номер месяца, %Y - год. По умолчанию: %b, %Y
timefmt = '%b, %Y'
 
# send timefmt
# Формат отображения дат.  %d - день, %b - месяц, %m - номер месяца, %Y - год. По умолчанию: %b, %Y
send_timefmt = '%b, %Y'
 
# to lowercase
# Преобразовать пути в нижний регистр.
to_lowercase = False
 
# replace whitespace
# Заменить пробел символом подчеркивания.
replace_whitespace = False
 
# single dir
# Сохранить в одной директории, игнорируя шаблонную структуру директории
single_dir = False
 


