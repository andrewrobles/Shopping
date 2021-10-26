import { useState } from 'react';
import styles from '../styles/Home.module.css'

export default function Home() {
  const [state, setState] = useState({ show: false })

  const toggleModal = () => {
    setState({
      show: !state.show
    })
  }

  return (
    <div className={styles.container}>
      <button id={'add-item-button'} className={styles.blueButton} onClick={ () => { toggleModal() }}>Add your first item</button>
      <Modal show={state.show} hide={toggleModal}/>
    </div>
  )
}

function Modal(props) {
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
      alert(message)
    }
   

    if (!props.show){
      return null
    } else return (
      <div>
        <button onClick={() => props.hide()}>Hide</button>
        <div>Hello Modal</div>
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
