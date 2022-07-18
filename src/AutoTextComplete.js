import './auto-text-complete.css';
import React, { useState } from 'react';

const AutoTextComplete = () => {
  const [inputText, setInputText] = useState('')
  const [words, setWords] = useState([])

  const onChange = (event) => {
    const { value } = event.target
    setInputText(value)
    if (value === ''){
      setWords([])
    }
    if (value) {
      try {
        setTimeout(() => {
          console.log('Fetching words...')
          fetch(`http://127.0.0.1:7000/prefix/${value}`, { mode: 'cors'})
          .then(res => res.json())
          .then(data => {
            let tempWords = []
            for (const [key] of Object.entries(data)) {
              tempWords.push(key)
            }
            setWords(tempWords)
          })
        }, 500)
      } catch(error) {
        console.log(error);
      }
    }
  };

  const renderList = (word, index) => {
    return (
      <li className={'dropdown-item'} name={word} value={word} key={index}>
          <label className='dropdown-item-label'>{word}</label>
      </li>
    )
}

  return (
    <div>
      <div className='header'>
        <h2>Auto text complete input</h2>
      </div>
      <div className='auto-text-dropdown-container'>
        <div className='auto-text-field'>
          <input type="text" id="auto-text" name="auto-text" onChange={(e)=> onChange(e)}></input>
          {inputText && <div className='auto-text-field-dropdown'>
            <ul className='dropdown-items'>
              {
                words && words.length > 0 && words.map((word, index)=> {
                        return (
                          renderList(word, index)
                        )
                      })
              }
            </ul>
          </div>}
        </div>
      </div>
    </div>
  );

}

export default AutoTextComplete;
