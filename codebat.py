# warmup-1 
# sleep-in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
  # monkey-trouble
def monkey_trouble(a_smile, b_smile):
  if ((a_smile == True and b_smile == True) or  (a_smile == False and b_smile == False)):
    return True
  else:
    return False
# sum_double
def sum_double(a, b):
 
  sum = a + b
  
  
  if a == b:
    sum = sum * 2
  return sum
# diff21
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    
    return (n - 21) * 2
# parrot_trouble
def parrot_trouble(talking, hour):
  if (talking == True and (hour  in range(0, 7) or hour in range(21, 24))):
    return True
  else:
    return False
# makes10
def makes10(a, b):
  if(a == 10 or b == 10 or a+b==10):
    return True
  else:
    return False
# near_hundred
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
#  pos_neg
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
# not_string
def not_string(str):
  if (str[:3] == "not"):
    return str
  else:
    return "not " + str
# missing_char
def missing_char(str, n):
    front = str[:n]  
    back = str[n+1:] 
    return front + back
# front_back
def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1] 
  

  return str[len(str)-1] + mid + str[0]
  # front3
  def front3(str):
  
    front_end = 3
    if len(str) < front_end:
        front_end = len(str)
  front = str[:front_end]
  return front + front + front 

# warmup-2
# string_times
def string_times(str, n):
  result=""
  for i in range(n):
    result+=str
  return result
# front_times
def front_times(str, n):
  l = str[:3]
  result=""
  if len(str) > 3:
    for i in range(n):
        result+=l
    
  else:
    for i in range(n):
      result+=str
  return result
# string_bits
def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i  % 2 == 0:
      result+=str[i]
  return result
# string_splosion
def string_splosion(str):
  result = ""
  n = len(str)
  for i in range(n):
    result+=str[:i+1]
  return result
# last2
def last2(str):
  
  if len(str) < 2:
    return 0
  
  
  last2 = str[len(str)-2:]
  count = 0
  
  
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count
# array_count9
def array_count9(nums):
  count=0
  for i in range(len(nums)):
    if (nums[i] == 9):
      count+=1
  return count
#array_front9
def array_front9(nums):
  
  if (len(nums) <= 4):
    for i in range(len(nums)):
      if (nums[i] == 9):
        return True
  elif (len(nums) > 4):
    
    for i in range(4):
      if (nums[i] == 9):
        return True
  return False
# array123
def array123(nums):
  for i in range(len(nums)-2):
    if (nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
      return True
  return False
#string_match
def string_match(a, b):

  shorter = min(len(a), len(b))
  count = 0
  
  
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count
  # String-1
  # hello_name
def hello_name(name):
  return ("Hello " + name + "!")
  #make_abba
def make_abba(a, b):
  return a+b+b+a
  # make_tags
def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"
#make_out_word
def make_out_word(out, word):
  return out[0:len(out)/2]+word+out[len(out)/2:len(out)]
# extra_end
def extra_end(str):
  result = ""
  for i in range(3):
     result+=str[len(str)-2:len(str)]
  return result
# first_two
def first_two(str):
  if (len(str) < 2):
    return str
  else:
    return str[:2]
# first_half
def first_half(str):
  return str[:len(str)/2]
# without_end
def without_end(str):
  result = str[1 :len(str)-1]
  return result
# combo_string
def combo_string(a, b):
  short = min(len(a), len(b))
  
  if (len(a) == short):
    return a+b+a
  else:
    return b+a+b
# non_start
def non_start(a, b):
  return a[1: len(a)]+b[1: len(b)]
# left2
def left2(str):
  result = ""
  chars = str[:2]
  if (len(str) > 2):
    result = str[2: len(str)] + chars
  else:
    result = str
  return result
# first_last6
def first_last6(nums):
  if (len(nums) >= 1):
    if (nums[0] == 6 or nums[len(nums)-1] == 6):
      return True
  else:
    if (nums[0] == 6):
      return True
  return False
# same_first_last
def same_first_last(nums):
  if (len(nums)>=1 and nums[0] == nums[len(nums) -1]):
    return True
  return False
# make_pi
def make_pi():
  s = []
  s.append(3)
  s.append(1)
  s.append(4)
  return s
# common_end
def common_end(a, b):
  if a[0] == b [0] or a[len(a)-1] == b[len(b)-1]:
      return True
  else:
    return False
# sum3
def sum3(nums):
  sum = 0
  for i in range(len(nums)):
    sum+=nums[i]
  return(sum)
# rotate_left3
def rotate_left3(nums):
  s = []
  temp = nums[0]
  for i in range(1,3):
    s.append(nums[i])
    
  s.append(temp)
  return s
# reverse3
def reverse3(a):
  for i in range(len(a)//2):
        temp = a[i]
        a[i] = a[len(a)-i-1]
        
        a[len(a)-i-1] = temp
  return a
# max_end3
def max_end3(nums):
  maxi = max(nums[0], nums[2])
  for i in range(len(nums)):
    
    nums[i] = maxi
  return nums
# sum2
def sum2(nums):
  sum = 0
  if (len(nums) <= 2):
    for i in range(len(nums)):
      sum+=nums[i]
  else:
      for i in range(0, 2):
        sum+=nums[i]
  return sum
    
# middle_way
def middle_way(a, b):
  s = []
  s.append(a[len(a)/2])
  s.append(b[len(b)/2])
  return s
# make_ends
def make_ends(nums):
  s = []
  s.append(nums[0])
  s.append(nums[len(nums)-1])
  return s
# has23
def has23(nums):
  for i in range(len(nums)):
    if (nums[i] == 2 or nums[i] == 3):
      return True
    else:
      return False
# cigar
def cigar_party(cigars, is_weekend):
  if (cigars in range(40, 61)):
    return True
  elif (is_weekend and cigars >=40):
    
      return True
  else:
    return False
# date_fashion
 def date_fashion(you, date):

  if (you <= 2 or date <= 2):
    return 0
  elif (you >= 8 or date >=8):
    return 2
  else:
    return 1
# squirrel_play
def squirrel_play(temp, is_summer):
   if (temp >= 60 and temp <= 90):
    return True
   elif (is_summer and temp >= 60 and temp <= 100):
     return True
   else:
      return False
# caught_speeding
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if (speed <=65):
      return 0
    elif (speed <=85 and speed >=66):
      return 1
    elif speed >= 86:
      return 2
   
    
  elif speed <= 60:
    return 0
  elif speed in range(61, 81):
    return 1
  else:
    return 2
  
# sorta_sum
def sorta_sum(a, b):
  if (a+b in range(10, 20)):
    return 20
  else:
    return a+b
# alarm_clock
def alarm_clock(day, vacation):
   if (vacation):
    if day in range(1, 6):
      return "10:00"
    else:
      return "off"
   else:
      if day in range(1, 6):
        return "7:00"
      else: 
        return "10:00"
# love6
def love6(a, b):
  if (a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6):
    return True
  else:
    return False
# in1to10
def in1to10(n, outside_mode):
  
  if(n>1 and n<10):
    return not outside_mode
  else:
    return outside_mode or n is 10 or n is 1
# near_ten
def near_ten(num):
  if num % 10 <= 2 or num % 10 >= 8:
    return True
  else:
    return False
# logic-2
# def make_bricks(small, big, goal):
  if (goal//5 <= big) and ((goal - 5*(goal//5))<= small):
    return True
  elif (goal//5 >= big) and ((goal - 5*(big)) <= small):
    return True
  return False
# lone_sum
def lone_sum(a, b, c):
   if (a == b and a == c and c == b):
     return 0
   elif (a == b):
      return c
   elif (b == c):
      return a
   elif ( a == c):
      return b
   else:
      return a+b+c
# lucky_sum
def lucky_sum(a, b, c):
    if ( a == 13):
      return 0
    elif (b == 13):
      return a
    elif (c == 13):
      return a+b
    return a+b+c
# no_teen_sum
def no_teen_sum(a, b, c):
    return fix_teen(a)+fix_teen(b)+fix_teen(c)
  
def fix_teen(n):
   return n if n not in [13,14,17,18,19] else 0
# round_sum
def round_sum(a, b, c):
   return round10(a)+round10(b)+round10(c)

def round10(num):
   return (num+5)/10*10
# close_far
def close_far(a, b, c):
  return (abs(abs(b)-abs(c))>=2) and \
  ((abs(abs(b)-abs(a))<=1 and abs(abs(c)-abs(a))>=2) \
  or (abs(abs(c)-abs(a))<=1 and abs(abs(b)-abs(a))>=2))
# make_chocolate
def make_chocolate(small, big, goal):
  if goal >= 5 * big:
        remainder = goal - 5 * big
  else:
        remainder = goal % 5
        
  if remainder <= small:
        return remainder
        
  return -1
# String-2 
# double_char
def double_char(str):
  s = ""
  for i in range(len(str)):
    s += str[i] + str[i]
  return s
# count_hi
def count_hi(str):
  sum = 0
  for i in range(len(str)-1):
    if (str[i] == "h" and str[i+1] == "i"):
      sum +=1
  return sum
# cat_dog
def cat_dog(str):
  a = str.split('cat')
  b = str.split('dog')
  if len(a) == len(b):
    return True
  else:
    return False
# count_code
def count_code(str):
  result = 0
  for i in range(len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      result += 1
  return result
# end_other
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))

# xyz_there
def xyz_there(str):
  str = str.replace('.xyz', '')
  if 'xyz' in str:
    return True
  else:
    return False
# List-2
# count_evens
def count_evens(nums):
  sum = 0
  for i in range(len(nums)):
    if (nums[i]  % 2 == 0):
      sum +=1
  return sum
# big_diff
def big_diff(nums):
  maxx = nums[0]
  minn = nums[0]
  for i in range(len(nums)):
    if nums[i] > maxx:
      maxx = nums[i]
    if nums[i] < minn:
      minn = nums[i]
  return maxx - minn
# centered_average
def centered_average(nums):
  total = 0
  number_of_excepts = 2
  centered = nums
  centered.remove(max(nums))
  centered.remove(min(nums))
  for i in centered:
    total += i
  return total/len(centered)

# sum13
def sum13(nums):
  sum = 0
  for i in range(0, nums.count(13)):
    if nums.count(13):
      after = nums.index(13)
      nums.remove(13)
    if after < len(nums):
      nums.pop(after)
  for i in nums:
    sum += i
  return sum

# sum67
def sum67(nums):
  dontadd = 0
  sum = 0
  for i in range(0, len(nums)):
    if dontadd == 0:
      if nums[i] == 6:
        dontadd = 1
      else:
        sum += nums[i]
    else:
      if nums[i] == 7:
        dontadd = 0
      else:
        pass
  return sum

# has22
def has22(nums):
  indices = []
  for i in range(0, len(nums)):
    if nums[i] == 2:
      indices.append(i)
  for i in range(0, len(indices)-1):
    if indices[i+1] - indices[i] == 1:
      return True
  return False


      

     
      