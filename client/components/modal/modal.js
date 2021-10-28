import {useState} from 'react'
import styles from './modal.module.css'

export default function Modal() {
    const [state, setState] = useState({ 
        show: false,
        items: []
      })
    
      const toggleModal = () => {
        setState({
          show: !state.show,
          items: state.items
        })
      }

    return <div className={styles.modal}>
        <button id={'add-item-button'} className={styles.blueButton} onClick={ () => { toggleModal() }}>Add your first item</button>
        <Form show={state.show} hide={toggleModal}/>
    </div>
}

function Form(props) {
    const [state, setState] = useState({
      'itemName': '',
      'description': '',
      'amount': 1
    })
  
    const handleChange = (e) => {
      const name = e.target.name
      const value = e.target.value
      setState(prevState => {
        const newState = {...prevState}
        newState[name] = value;
        return newState
      })
    }
  
    const addItem = () => {
      const message = state.itemName + state.description + state.amount
      fetch('http://localhost:8000/item/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(state)
      })
      .then(response => response.json())
      .then(data => console.log(data));
  
      props.hide()
    }
    
  
    if (!props.show){
      return null
    } else return (
      <div>
        <button onClick={() => props.hide()}>Hide</button>
        <input name="itemName" onChange={handleChange}></input>
        <input name="description" onChange={handleChange}></input>
        <select name="amount" onChange={handleChange} id="amount">
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
        </select>
        <button onClick={addItem}>Add Item</button>
      </div>
    )
  }