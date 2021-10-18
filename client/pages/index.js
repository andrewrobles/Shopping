import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <button className={styles.blueButton}>Add your first item</button>
    </div>
  )
}
