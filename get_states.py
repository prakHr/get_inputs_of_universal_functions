from x import X
from pprint import pprint
import os


def get_final_state_of_universal_function(fn,input_state):
    output_state = fn(*input_state)
    return output_state

def get_final_state_of_universal_functions(fns,input_states):
    output_states = []
    for fn,input_state in zip(fns,input_states):
        output_state = get_final_state_of_universal_function(fn,input_state)
        output_states.append(output_state)
    return output_states

# if __name__=="__main__":
#     sqr = [
#         X+X,
#         X+X,
#         X**X**X,
#         X**X + X**X,
#         X + X,
#         X + X**X + X**X**X + X**X**X**X
#     ]
#     actual_index = 2
#     zero_based_index = actual_index - 1
#     input_state = [
#         [
#             [1],
#             [1,2,3][zero_based_index:]
#         ],
#         [
#             [1],
#             [2,3]
#         ],
#         [3,1,1],
#         [3,2,4,2],
#         [3,3],
#         [1,1,1,1,1,1,1,1,1,1]
#     ]
#     answer = get_final_state_of_universal_function(sqr[0],input_state[0])
#     print(answer)
#     answers = get_final_state_of_universal_functions(sqr,input_state)
#     print(answers)

