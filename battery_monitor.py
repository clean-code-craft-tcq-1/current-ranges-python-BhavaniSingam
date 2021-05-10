def current_ranges(range_list):   
  if validate_input(range_list):
      list1 = []
      while len(range_list)>1:
          seq_list,range_list = get_range_sequence(range_list)
          add_to_list(seq_list,list1)
      if list1:    
          get_output(list1)
          return 'Valid Input'
  return 'Invalid Input'       
    
def get_range_sequence(range_list):
    count = 0 
    seq = []      
    for i in range_list:          
      if len(seq) == 0:
        seq.append(i)
        count+= 1
      elif i == seq[count - 1] or i == (seq[count - 1])+1:
        seq.append(i)
        count+= 1
      else: 
        break
    seq,newRangeList = get_list(range_list,seq,count)
    return seq,newRangeList
             
def get_list(range_list,sequence,count):
    newRangeList = []    
    if (len(range_list) - count)> 0:
        newRangeList = range_list[count:]    
    return sequence,newRangeList           
                    
def add_to_list(sequence_list,list_t):
    if len(sequence_list) > 1:              
        return(list_t.append(sequence_list))
    else:
        return False
  
def validate_input(ranges):
    return (len(ranges)>0)

def get_output(list_t):
    for lst in list_t:
        reading = len(lst)
        ranges = str(lst[0]) + '-' + str(lst[len(lst) - 1])
        output = str(ranges) + ',' + str(reading)
        print(output)
    return output
