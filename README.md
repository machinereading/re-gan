# Korean Relation Extraction using GAN

## About
Korean Relation Extraction using GAN

## Introduction
It is based on [AtNRE](https://github.com/jxwuyi/AtNRE) model. 
The following have been modified:
1) Link [ELMo](https://github.com/allenai/bilm-tf) and GAN networks
2) Add Twitter tokenizer to adjust Korean (use `/data/kaist/embedding/fasttext/vector_np_100d_wikipedia.pkl`)

## How to use
refer `script_kaist_adv.sh` files
<br>and<br>
OPTION descriptions are in `bag_runner.py` such as model_name, epochs, vocab_size, cell_type, etc.

### How to run
`script_kaist_adv.sh`
<br>or<br>
`python3 bag_runner.py [OPTIONS]`

### Data Example
```
22일 영국 <e2>맨체스터</e2>시 <e1>맨체스터 아레나</e1>에서 자폭 테러로 의심되는 폭탄 테러가 발생하면서 유럽이 다시 한번 테러 공포에 떨고 있다.,location
```
CSV format; sentence with two target entities, relation

## Licenses
* `CC BY-NC-SA` [Attribution-NonCommercial-ShareAlike](https://creativecommons.org/licenses/by-nc-sa/2.0/)
* If you want to commercialize this resource, [please contact to us](http://mrlab.kaist.ac.kr/contact)

## Publisher
[Machine Reading Lab](http://mrlab.kaist.ac.kr/) @ KAIST

## Acknowledgement
This work was supported by Institute for Information & communications Technology Promotion(IITP) grant funded by the Korea government(MSIT) (2013-0-00109, WiseKB: Big data based self-evolving knowledge base and reasoning platform)
