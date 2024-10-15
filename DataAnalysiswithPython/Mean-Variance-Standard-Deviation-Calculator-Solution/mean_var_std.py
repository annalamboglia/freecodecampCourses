import numpy as np

def calculate(list):
  calculations={'mean': [],'variance': [], "standard deviation": [],\
                'max': [],'min': [], "sum": []}

  try:
    len(list) == 9

    array=np.asarray(list)
    arr=array.reshape((3,3))
    
    calculations['mean'].append(np.mean(arr, axis = 0))
    calculations['mean'].append(np.mean(arr, axis = 1))
    calculations['mean'].append(np.mean(array))
  
    calculations['variance'].append(np.var(arr, axis = 0))
    calculations['variance'].append(np.var(arr, axis = 1))
    calculations['variance'].append(np.var(array))
    
    calculations['standard deviation'].append(np.std(arr, axis = 0))
    calculations['standard deviation'].append(np.std(arr, axis = 1))
    calculations['standard deviation'].append(np.std(array))
  
    calculations['max'].append(np.max(arr, axis = 0))
    calculations['max'].append(np.max(arr, axis = 1))
    calculations['max'].append(np.max(array))
  
    calculations['min'].append(np.min(arr, axis = 0))
    calculations['min'].append(np.min(arr, axis = 1))
    calculations['min'].append(np.min(array))
    
    calculations['sum'].append(np.sum(arr, axis = 0))
    calculations['sum'].append(np.sum(arr, axis = 1))
    calculations['sum'].append(np.sum(array))
    return calculations
  
  except ValueError:
    print('List must contain nine numbers.')

