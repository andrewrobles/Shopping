import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import styles from './index.module.css'

import quizQuestionData from '../quizQuestionData'
import Navbar from '../components/Navbar/Navbar'
import Header from '../components/Header/Header'
import Content from '../components/Content/Content'
import Control from '../components/Control/Control'
import Results from '../components/Modal/Modal'
import Button from '../components/Button/Button'

const quizTitle='Weird Text Format Encoder'
const quizDescription='Type in the word you would like to encode'
const estimatedTime='30 minutes'
const difficultyLevel='6'
const answerKey=['a1', 'b2', 'c3', 'd4', 'e4']

export default function Home() {
  const [state, setState] = useState({
    // -1 indicates quiz has not started
    'questionIndex': -1,
    'quizQuestionData': quizQuestionData,
    // -1 indicates question has not yet been answered
    'studentAnswers': Array(quizQuestionData.length).fill(-1)
  })

  const selectQuestionOption = (questionIndex, optionId) => {
    // studentAnswers maps to question and value maps to answer
    const studentAnswers = state.studentAnswers

    studentAnswers[questionIndex] = optionId

    setState({
      'questionIndex': state.questionIndex,
      'quizQuestionData': state.quizQuestionData,
      'studentAnswers': state.studentAnswers
    })
  }

  const nextQuestion = () => {

    // Out of bounds check
    if (state['questionIndex'] + 1 < state.quizQuestionData.length) {

      // Go to next question
      setState({
        'questionIndex': state['questionIndex'] + 1,
        'quizQuestionData': state.quizQuestionData,
        'studentAnswers': state.studentAnswers
      })
    }
  }

  return (
    <div className={`${styles.index}`}>
        <Navbar/>
      <div className={`container`}>
          <div className={`mt-5`}>
            <Header 
              quizTitle={quizTitle}
              quizDescription={quizDescription}
              questionIndex={state.questionIndex}
            />
          </div>
          <Status
              questionIndex={state.questionIndex}
              quizLength={quizQuestionData.length}
          />

          <div className="form-group">
              <input type="email" className={`${styles.field} form-control border-light`} id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Example: tacocat"/>
          </div>
          <div className={`pt-4`}></div>
          <div>
            <Button buttonText={'Execute'}/>
          </div>
      </div>
    </div>
  )
}

function Status(props) {
  const keys = [...Array(props.quizLength).keys()]
  if (props.questionIndex >=0 ) {
    // Add one to zero indexed question number
    return <div>
      <div class="d-flex flex-row-reverse">
        <div class="p-2"><nav aria-label="Page navigation example">
            <ul class="pagination">
              {
                keys.map(currKey => currKey == props.questionIndex ? 
                <li class="page-item active"><a class="page-link" href="#">{currKey + 1}</a></li>:
                <li class="page-item"><a class="page-link" href="#">{currKey + 1}</a></li>)
              }
            </ul>
          </nav>
        </div>
      </div>
    </div>
  } else return <></>
}