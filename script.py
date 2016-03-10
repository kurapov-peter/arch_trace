import string
import operator

arifmetics = ['add', 'addi', 'addiu', 'addu', 'clo', 'clz', 'dadd', 'daddi',
'daddiu', 'daddu', 'dclo', 'dclz', 'ddiv', 'ddivu', 'div', 'divu', 'dmult',
'dmultu', 'dsub', 'dsubu', 'madd','maddu', 'msub', 'msubu', 'mul', 'mult',
'multu', 'slt', 'slti', 'sltiu', 'sltu', 'sub', 'subu']

branch = ['b', 'bal', 'beq', 'bgez', 'bgezal', 'bgtz','bgtzl', 'blez', 'bltz', 'bltzal', 'bne', 'j', 'jal',
'jalr', 'jr', 'beql', 'bgezall', 'bgezl', 'blezl', 'bltzall', 'bltzl', 'bnel', 'bc1f', 'bc1fl', 'bc1t', 'bc1tl']

load_store = ['lb', 'lbu', 'ld', 'ldl', 'ldr', 'lh',
'lhu', 'll', 'lld', 'lw', 'lwl', 'lwr', 'lwu', 'pref', 'sb', 'sc', 'scd', 'sd','sw', 'sdl', 'sdr', 'sh', 'swl', 'swr', 'sync', 'ldc1',
'ldxc1', 'lwc1', 'lwxc1', 'prefx', 'sdc1', 'sdxc1', 'swc1', 'swxc1']

logic = ['and', 'andi', 'lui', 'nor', 'or', 'ori', 'xor', 'xori', 'dsll', 'dsll32',
'dsllv', 'dsra', 'dsra32', 'dsrav', 'dsrl', 'dsrl', 'dsrl32', 'dsrlv', 'sll', 'sllv', 'sra', 'srav', 'srl', 'srlv']

move = ['mfhi', 'mflo', 'movf', 'movn', 'movt', 'movz', 'mthi', 'mtlo']

floating = ['abs.fmt',
'add.fmt', 'div.fmt', 'madd.fmt', 'msub.fmt', 'mul.fmt', 'neg.fmt', 'nmadd.fmt', 'recip.fmt',
'rsqrt.fmt', 'sqrt.fmt', 'sub.fmt', 'c.fmt', 'ceil.fmt', 'cvt.fmt', 'floor.fmt', 'round.fmt', 'trunc.fmt',
'cfc1.fmt', 'ctc1.fmt', 'dmfc1.fmt', 'dmtc1.fmt', 'mtc1.fmt', 'mfc1.fmt', 'mov.fmt', 'movf.fmt',
'movn.fmt', 'movt.fmt', 'movz.fmt']

nope = ['nop', 'ssnop']

#ctc1 - check!
privileged = ['cache', 'cfc0', 'ctc0', 'dmfc0', 'dmtc0', 'eret', 'mfc0',
'mtc0', 'tlbp', 'tlbr', 'tlbwi', 'tlbwr','wait','ctc1']


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def instruction_annotation(x):
    if x in arifmetics:
        return 'A'
    elif x in branch:
        return 'B'
    elif x in load_store:
        return 'S'
    elif x in logic:
        return 'L'
    elif x in move:
        return 'M'
    elif x in floating:
        return 'F'
    elif x in nope:
        return 'N'
    elif x in privileged:
        return 'P'
    elif x == 'E':
        return x
    else :
        return '0'

        
def get_values(lVals):
    res = []
    for val in lVals:
        if type(val) not in [list, set, tuple]:
            res.append(val)
        else:
            res.extend(get_values(val))
    return res

f = open("log2.txt", "r").read().split('\n')

data = [",".join(f[i].split()) for i in range(len(f))]
data = [data[i].split(',') for i in range(len(f))]

databkp = data

print len(data)
#DELETE HEADER
for x in data:
    if 'START' not in x:
        del x
if not data:
    #VERY BAD FOR PERFORMANCE
    #DELETE THIS FUNCTIONALITY FIRST IF APP IS TOO SLOW
    data = data1

exceptions = [i+1 for i in range(0, len(data)) if 'Exception' in data[i]]
eret       = [i for i in range(0, len(data)) if 'eret' in data[i]]
mask       = [range(i,j+1) for (i,j) in list(zip(exceptions, eret))]
mask = list(set(range(1,len(data))) - set(get_values(mask)))

#print mask
# DELETE EXCEPTION INSTRUCTIONS
data = [data[i] for i in mask]




for i in range(0, len(data)) :
    if 'Exception' in data[i]:
        data[i][4] = 'E'

# CHECK FOR BUG
#print len(data)
#for i in range(0, len(data)-1):
#    if data[i][0].isdigit():
#        if instruction_annotation(data[i][4]) == '0':
#            print data[i]


data_prepared = [data[i][4] for i in range(0,len(data)-1) if data[i][0].isdigit()]
data_prepared = list(chunks([instruction_annotation(i) for i in data_prepared], 4))[:-1]
data_prepared = ["".join(i) for i in data_prepared]
data_prepared = dict((x,data_prepared.count(x)) for x in set(data_prepared))
#print data_prepared

data_prepared = dict((key,val) for key,val in data_prepared.iteritems() if 'E' not in key or key[:-1] == 'E')
data_prepared = sorted(data_prepared.items(), key=operator.itemgetter(1), reverse=True)

print data_prepared



