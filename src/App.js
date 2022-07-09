import './App.css';
import React from 'react';

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      value: '',
      suggestions: []
    };
  }

  onChange = (event) => {
    this.setState({
      value: event.target.value
    });
  };
  
  onSuggestionsFetchRequested = ({ value }) => {
    this.setState({
      // suggestions: getSuggestions(value)
    });
  };

  onSuggestionsClearRequested = () => {
    this.setState({
      suggestions: []
    });
  };

  render() {
    const { value } = this.state;
    console.log(value)
    return (
      <div>
        <p>AUTO COMPLETE TEXT INPUT</p>
        <div className='auto-text-field'>
          <input type="text" id="auto-text" name="auto-text" onChange={(e)=> this.onChange(e)}></input>
        </div>
      </div>
    );
  }
}

export default App;
