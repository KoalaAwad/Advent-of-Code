fs = require 'fs'

FileRead = fs.readFileSync("chal1.txt", 'utf8')

NumberDictionary = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven','eight','nine']

lines = FileRead.split '\n'

BackChecking = (x) ->
  for a in [x.length - 1 .. 0]
    if x[a].match(/\d/)
      return x[a]
    else
      IndexDict = 0
      for word in NumberDictionary
        IndexDict += 1
        length = word.length

        if x[a] == word[length - 1]
          index1 = (a + 1) - length
          CheckWord = x[index1..a]
          
          if CheckWord == word
            return IndexDict - 1

Checking = (x) ->
  index = 0
  for a in x
    if a.match(/\d/)
      return a
    
    IndexDict = 0
    for word in NumberDictionary
      IndexDict += 1
      
      if a == word[0]
        length = word.length
        index1 = index + length
        CheckWord = x[index...index1]
        
        if CheckWord == word
          return IndexDict - 1

    index += 1

main = ->
  sum = 0
  for word in lines
    Output = Checking word
    BackOutput = BackChecking word

    console.log "#{Output}#{BackOutput}"
    sum += parseInt "#{Output}#{BackOutput}"

  console.log sum

main()
