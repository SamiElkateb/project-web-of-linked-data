report: 
	@pandoc -o rapport.pdf -V colorlinks=true -V linkcolor=blue  rapport.md

merge_data:
	cat project/*.ttl > all_data.ttl
