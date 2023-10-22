import cohere 
import os
import re

api_key = 'y7Pemp9bBQAX1DUwtP8bFtKssS4qSudAlzhQh87S'
co = cohere.Client(api_key)
# model = 'command-nightly'
model = 'f2e29a92-b7c1-44b0-8344-610a442ac4d2-ft'

def write_to_file(response_text, base_filename="output_response.txt"):
    # Verifica se o arquivo já existe
    if os.path.exists(base_filename):
        # Se o arquivo existir, encontre um novo nome de arquivo
        index = 1
        while os.path.exists(f"{index}_{base_filename}"):
            index += 1
        filename = f"{index}_{base_filename}"
    else:
        filename = base_filename
    
    # Escreve o texto no arquivo
    with open(filename, 'w') as file:
        file.write(response_text)
    print(f"Response written to: {filename}")


prompt = '''
Below, I will give a song on an specified structure. 
In first metadata gives the name of the original song (You must change this on your answer).
In second metadata  gives the tags relationated to the song.
In third metadata gives the energy's song. If they aren't 'None' they talk some about the energy of the song.
The last metadata gives a sequence of three columns.
The strucuture of those three columns is very important. The description about how they works is: First one is the initial time of the chord, the second is the final time of the chord and the third is the chord by itself.

You must follow the exact same structure.

Generate a similar song to the one below. You must change the times of the columns and the chords to change the song by complete. Furthermore you have to change the original topic field and original energy field to new ones, because they will talk about the new song you generated.

metadata:
original music: Queen - Don't Stop Me Now
original topic: feelings
original energy: 0.80
the melody  starts here:
0.000	0.563	N
0.563	3.306	F:maj
3.306	5.810	A:min7
5.810	8.331	D:min7
8.331	10.675	G:min7
10.675	13.155	C
13.155	15.539	F:maj
15.539	17.915	F:7
17.915	20.379	Bb
20.379	22.860	G:min7
22.860	25.217	D:7
25.217	26.041	G:min
26.041	26.593	D:min
26.593	27.133	G:min
27.133	29.867	G:min7
29.867	30.731	G:min
30.731	31.254	D:min
31.254	33.717	G:min
33.717	35.288	C:7
35.288	36.832	F:maj
36.832	38.371	A:min7
38.371	39.976	D:min7
39.976	41.512	G:min7
41.512	43.027	C:7
43.027	44.640	F:maj
44.640	46.124	A:min
46.124	47.673	D:min
47.673	49.217	G:min7
49.217	50.743	C:7
50.743	52.304	F:maj
52.304	53.859	F:7/b7
53.859	55.415	Bb:maj
55.415	56.901	G:min7
56.901	58.335	D:7
58.335	60.024	G:min
60.024	61.592	D:7
61.592	63.461	G:min7
63.461	63.861	F/3
63.861	64.473	Bb
64.473	66.163	C:maj
66.163	66.732	F:maj
66.732	67.150	G:min
67.150	67.545	F/3
67.545	69.263	D:min
69.263	70.796	G:min7
70.796	72.328	C
72.328	72.886	F:maj
72.886	73.280	G:min
73.280	73.675	F/3
73.675	75.370	D:min
75.370	76.926	G:min7
76.926	78.435	D:7
78.435	78.992	G:min
78.992	79.363	D:min
79.363	81.478	G:min7
81.478	82.105	G:min
82.105	82.476	D:min
82.476	84.492	G:min7
84.492	86.060	C
86.060	89.135	Bb:sus4
89.135	90.689	F:maj
90.689	92.245	A:min7
92.245	93.777	D:min7
93.777	95.310	G:min7
95.310	96.849	C:7
96.849	98.398	F:maj
98.398	99.977	A:min
99.977	101.494	D:min
101.494	103.088	G:min7
103.088	104.598	C:7
104.598	106.069	F:maj
106.069	107.616	F:7
107.616	109.195	Bb:maj
109.195	110.704	G:min7
110.704	112.237	D:7
112.237	113.755	G:min
113.755	115.314	D:7
115.314	117.241	G:min7
117.241	117.641	F/3
117.641	118.227	Bb
118.227	118.624	C
118.624	133.589	N
133.589	135.191	F:maj
135.191	136.724	A:min
136.724	138.210	D:min
138.210	139.765	G:min
139.765	141.298	C:maj
141.298	142.877	F:maj
142.877	144.433	A:min
144.433	145.988	D:min
145.988	147.544	G:min
147.544	149.007	C:maj
149.007	150.516	F:maj
150.516	152.078	F:7
152.078	153.657	Bb:maj
153.657	155.190	G:min7
155.190	156.746	D:7
156.746	158.255	G:min
158.255	159.825	D:7
159.825	161.690	G:min7
161.690	162.092	F/3
162.092	162.653	Bb
162.653	164.348	C:maj
164.348	164.928	F:maj
164.928	165.323	G:min
165.323	165.741	F/3
165.741	167.459	D:min
167.459	169.015	G:min7
169.015	170.548	C:7
170.548	171.105	F:maj
171.105	171.500	G:min
171.500	171.871	F/3
171.871	173.613	D:min
173.613	175.122	G:min7
175.122	176.678	D:7
176.678	177.212	G:min
177.212	177.653	D:min
177.653	179.673	G:min7
179.673	180.300	G:min
180.300	180.671	D:min
180.671	182.831	G:min7
182.831	184.294	C:7
184.294	187.365	Ab
187.365	190.012	F
190.012	192.543	A:min
192.543	195.118	D:min
195.118	197.164	G:min7
197.164	199.927	C
199.927	202.272	F
202.272	204.594	F:7
204.594	206.870	Bb
206.870	209.470	A
209.470	211.733	N


A possible example that I can give to you is the one below.

relative music: Queen - Fat Bottomed Girls
relative tags: feelings
relative energy: 0.89
the melody starts here:
0.000	0.245	N
0.245	3.000	D:maj
3.000	4.233	G:sus4
4.233	5.804	G:maj
5.804	8.473	D:maj
8.473	9.967	G:sus4
9.967	11.384	A:maj
11.384	14.184	D:maj
14.184	16.743	G:maj
16.743	18.318	D:maj
18.318	18.837	A:maj
18.837	19.727	A:sus4
19.727	27.771	D:maj
27.771	35.898	D:maj
35.898	38.543	A:maj
38.543	41.282	D:maj
41.282	43.971	G:maj
43.971	45.298	D:maj
45.298	46.678	A:maj
46.678	52.506	D:maj
52.506	54.976	N
54.976	63.135	D:maj
63.135	65.811	A:maj
65.811	68.482	D:maj
68.482	71.150	G:maj
71.150	72.543	D:maj
72.543	73.890	A:maj
73.890	79.220	D:maj
79.220	80.563	C:maj
80.563	81.910	G/3
81.910	84.701	D:maj
84.701	86.025	C:maj
86.025	87.395	A:maj
87.395	90.135	D:maj
90.135	92.875	G:maj
92.875	94.176	D:maj
94.176	95.591	A:maj
95.591	96.923	D:maj
96.923	97.584	G:maj
97.584	98.355	F:maj
98.355	99.669	D:maj
99.669	101.095	A:maj
101.095	103.791	D:maj
103.791	105.294	G:7
105.294	106.647	D:maj
106.647	107.673	A:maj
107.673	109.306	D:maj
109.306	110.706	G:maj
110.706	112.178	D:maj
112.178	112.759	A:maj
112.759	113.153	D:maj
113.153	116.229	G:maj
116.229	124.556	D:maj
124.556	127.327	A:maj
127.327	130.129	D:maj
130.129	132.869	G:maj
132.869	134.192	D:maj
134.192	135.632	A:maj
135.632	136.931	D:maj
136.931	141.080	D:maj
141.080	142.380	C:maj
142.380	143.816	G/3
143.816	146.629	D:maj
146.629	148.023	C:maj
148.023	149.416	A:maj
149.416	152.188	D:maj
152.188	155.012	G:maj
155.012	156.376	D:maj
156.376	157.775	A:maj
157.775	158.739	D:maj
158.739	160.492	G:maj
160.492	161.839	D:maj
161.839	163.208	A:maj
163.208	200.431	D:maj
200.431	204.560	N
'''


def get_response_from_promissor_prompt():
    api_key = 'y7Pemp9bBQAX1DUwtP8bFtKssS4qSudAlzhQh87S'
    co = cohere.Client(api_key)

    prompt_path = 'prompt\prompt_5_promissorporra - sem resposta.txt'
    # Reading the entire file content at once
    with open(prompt_path, 'r') as file:
        prompt = file.read()

    model = 'command-nightly'
    # model = 'e0e24dd3-2818-4af4-b847-57a0f244e277-ft'
    # model = 'base'
    response = co.generate(  
        model=model,  
        prompt = prompt,
        # max_tokens=200, # This parameter is optional. 
        temperature=0.7,
        max_tokens=200)

    response = response.generations[0].text
    print('Prediction:\n{}'.format(response))
    return response

def generate_response(prompt : str):
    co = cohere.Client(api_key)
    response = co.generate(  
        model=model,  
        prompt = prompt,  
        # max_tokens=200, # This parameter is optional. 
        temperature=0.3)
    return response.generations[0].text

def write_to_file(response_text, base_filename="saidas_gustavo.txt"):
    # Verifica se o arquivo já existe
    if os.path.exists(base_filename):
        # Se o arquivo existir, encontre um novo nome de arquivo
        index = 1
        while os.path.exists(f"{index}_{base_filename}"):
            index += 1
        filename = f"{index}_{base_filename}"
    else:
        filename = base_filename
    
    # Escreve o texto no arquivo
    with open(filename, 'w') as file:
        file.write(response_text)
    print(f"Response written to: {filename}")

    response = response.generations[0].text
    print('Prediction: {}'.format(response))
    write_to_file(response, base_filename="output_response.txt")
    write_to_file(prompt, base_filename="prompt.txt")


def filter_table(output):

    # Using a regex to match lines that look like table rows
    table_lines = re.findall(r"([\d.]+)\s+([\d.]+)\s+(\S+)", output)

    # Joining each matching line with a newline character to get the table as a single string
    table_string = "\n".join(["   ".join(line) for line in table_lines])
    return table_string

if __name__ == "__main__":
    get_response_from_promissor_prompt()