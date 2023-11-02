colours = {
  "black": "\u001b[40m  ", 
  "white": "\u001b[47m  ", 
  "red": "\u001b[41m  ", 
  "green": "\u001b[42m  ", 
  "yellow": "\u001b[43m  ", 
  "blue": "\u001b[44m  ", 
  "magenta": "\u001b[45m  ", 
  "cyan": "\u001b[46m  "
}

black, white, red, green, yellow, blue, magenta, cyan = "\u001b[40m", "\u001b[47m", "\u001b[41m", "\u001b[42m", "\u001b[43m", "\u001b[44m", "\u001b[45m", "\u001b[46m"

for key in colours:
  value = colours[key]
  if key != "black":
    print(f"{key}: {value}\u001b[0m")
  else:
    print(f"{key}: {white + ' ' + black + '  ' + white + ' '}\u001b[0m")