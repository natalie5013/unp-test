lines = new File('anketa1').readLines()
lines.each {
	line = it.trim()
	if(line.length() == 0) return
	// println it
	if(line == 'да')
		println 'y'
	else if(line == 'нет')
		println 'n'
	else
		throw new RuntimeException("Unknown: $line")
}
