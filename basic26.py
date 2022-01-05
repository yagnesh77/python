def yagn( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '@'
          times = times - 1
        print(output)

yagn([5,6,7])

