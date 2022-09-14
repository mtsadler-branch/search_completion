import './auto-text-complete.css';
import React, { useState } from 'react';

const AutoTextComplete = () => {
  const [inputText, setInputText] = useState('')
  const [words, setWords] = useState([])
  const [synonyms, setSynonyms] = useState('')

  const onChange = (event) => {
    const { value } = event.target
    setInputText(value)
    if (value === ''){
      setWords([])
    }
    if (value) {
      try {
        setTimeout(() => {
          console.log('Fetching Suggestions for Prefix...')
          fetch(`http://localhost:5001/prefix/${value}/3`, { mode: 'cors'})
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


  const onClick = (event) => {
    const { textContent } = event.target
    if (textContent) {
      try {
          console.log('Fetching Description for Word...')
          fetch(`http://localhost:5001/details/${textContent}`, { mode: 'cors'})
          .then(res => res.json())
          .then(data => {
            setSynonyms(JSON.stringify(data))
          })
      } catch(error) {
        console.log(error);
      }
    }
  };

  const renderList = (word, index) => {
    return (
      <li className={'dropdown-item'} value={word} key={index} onClick={(e)=> onClick(e)}>
        {word}
      </li>
    )
}

  return (
    <div>
      <div className='header'>
        <h2>Shakespearean Auto-Complete</h2>
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
      <div className='footer'>
        { synonyms }
      </div>
    </div>
  );

}

export default AutoTextComplete;
