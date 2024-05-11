## Lets code a simple 1 neuron

## you get 3 inputs to the neuron 
## each input has a weight attached to it
## and 1 bias attached to neuron

input = [1, 2, 3]
weights = [2, 1.2, 1.3]
bias =  2

output = input[0] * weights[0] + input[1] * weights[1]+ input[2] * weights[2] + bias
print(output)

## lets code 3 neurons that takes 4 input
## here input will remain the same
## but weight and bias will be different for each neuron
input = [1,2,3]
weights1 = [2, 1.2, 1.3]
weights2 = [3, 1.5, 1.7]
weights3 = [4, 1.9, 1.8]

output_neuron1 = input[0] * weights1[0] + input[1] * weights1[1]+ input[2] * weights1[2] + bias
output_neuron2 = input[0] * weights2[0] + input[1] * weights2[1]+ input[2] * weights2[2] + bias
output_neuron3 = input[0] * weights3[0] + input[1] * weights3[1]+ input[2] * weights3[2] + bias

print(output_neuron1)
print(output_neuron2)
print(output_neuron3)

## lets refactor the above using loop
print("********* using loops ****************")
weights = [[2, 1.2, 1.3], [3, 1.5, 1.7], [4, 1.9, 1.8]]
biases = [2,2,2]
input = [1,2,3]
output = []

for i in range(len(input)):
    w = weights[i]
    bias = biases[i]
    o = 0
    for j in range(len(input)):
        o += input[j] * w[j]
    o += bias

    output.append(o)

print(output)

## lets refactor the above using zip function
print("********* using loops and zip function ****************")
weights = [[2, 1.2, 1.3], [3, 1.5, 1.7], [4, 1.9, 1.8]]
biases = [2,2,2]
input = [1,2,3]
output = []

for weight, bias in zip(weights,biases):
    o = 0
    for i in range(len(input)):
        o += input[i] * weight[i]
    o += bias        
    output.append(o)

print(output)