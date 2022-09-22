n = str(input())

pre_scale = n.split(' ')

scale = ('').join(pre_scale)

if scale == '12345678':
    print('ascending')
elif scale == '87654321':
    print('descending')
else:
    print('mixed')