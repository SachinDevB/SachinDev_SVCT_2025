def timeConversion(s):
     
    components = s[:-2].split(':')
    hh, mm, ss = map(int, components)
    
    
    if s[-2:] == 'PM' and hh != 12:
        hh += 12
    elif s[-2:] == 'AM' and hh == 12:
        hh = 0
    
  
    result = f'{hh:02d}:{mm:02d}:{ss:02d}'
    return result

 
input_time = "07:05:45PM"
output_time = timeConversion(input_time)
print(output_time)
