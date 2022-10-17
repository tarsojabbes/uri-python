while True:
  try:
    complaints = int(input())
    
    if (complaints > 0):
        print('vai ter duas!')
    else:
        print('vai ter copa!')
  except EOFError:
    break