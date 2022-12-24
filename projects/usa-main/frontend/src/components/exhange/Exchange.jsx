import React, { useState, useEffect } from 'react'
import s from './Exhange.module.css';
import { NavLink } from 'react-router-dom'
import Menu from '../menu/Menu';
import axios from 'axios';
import "./Exhange.css"

const Exchange = () => {

    const [exchangeState, setExchangeState] = useState({});

    const [exchangeStateBuy, setExchangeStateBuy] = useState({});

    const [inputMoney, setInputMoney] = useState(0)

    const [inputMoney2, setInputMoney2] = useState(0)
    const [selectedCurrency, setSelectedCurrency] = useState()
    const [selectedCurrency2, setSelectedCurrency2] = useState({})

    useEffect(() => {
        axios.get("/api/parsingexchange/").then(
            response => {
                console.log(response.data.data)
                setExchangeState({
                    activeObject: null,
                    objects: response.data.data
                })
                setExchangeStateBuy({
                    activeObject: null,
                    objects: response.data.data
                })
            }
        )

    }, [])

    const toggleActive = (index) => {
        setExchangeState({ ...exchangeState, activeObject: exchangeState.objects[index] })
        setSelectedCurrency(exchangeStateBuy.objects[index])
    }

    const toggleActive2 = (index) => {
        setExchangeStateBuy({ ...exchangeStateBuy, activeObject: exchangeStateBuy.objects[index] })
        setSelectedCurrency2(exchangeStateBuy.objects[index])
    }

    const toggleActiveStyle = (index) => {
        if (exchangeState.objects[index] === exchangeState.activeObject) {

            console.log(exchangeState.activeObject)
            return "active";
        } else {
            return "inactive";
        }
    }
    const toggleActiveStyle2 = (index) => {
        if (exchangeStateBuy.objects[index] === exchangeStateBuy.activeObject) {
            return "active";
        } else {
            return "inactive";
        }
    }

    const InputMoney = (e) => {
        e.preventDefault()
        setInputMoney(e.target.value)
        // setInputMoney2( inputMoney + 7)
        // console.log(inputMoney)
    }

    const trstFunc = (e) => {
        e.preventDefault()


        console.log(inputMoney)
        console.log(inputMoney2)
        console.log(selectedCurrency)
        console.log(selectedCurrency2)
        const rezult = selectedCurrency.buy_delta_positive / selectedCurrency2.buy_delta_positive * inputMoney
        console.log(rezult)
        setInputMoney2(+rezult.toFixed(2))

    }

    const checkState = () => {
        console.log(exchangeState)
    }

    return (
        <div className={s.wrapper}>
            <div className={s.menu}>
                <Menu />
            </div>
            <div className={s.mainBlock}>
                <div className={s.mainExchange}>

                    <div className={s.haveExchange}>
                        <div className={s.columndir}>
                            {exchangeState.objects && exchangeState.objects.map((elements, index) => {
                                return (
                                    <div key={index} className={toggleActiveStyle(index)} onClick={() => { toggleActive(index) }}>
                                        <p >{elements.currency}</p>
                                    </div>
                                )
                            })}

                        </div>
                        <h3>У меня есть</h3>
                        <input onChange={InputMoney} className={s.inputMoney} value={inputMoney} placeholder='введите сумму' />
                    </div>
                    <div className={s.haveExchange}>
                        <div className={s.columndir}>
                            {exchangeStateBuy.objects && exchangeStateBuy.objects.map((elements, index) => {
                                return (
                                    <div key={index} className={toggleActiveStyle2(index)} onClick={() => { toggleActive2(index) }}>
                                        <p >{elements.currency}</p>
                                    </div>
                                )
                            })}

                        </div>
                        <h3>Хочу приобрести</h3>
                        <input onChange={(e) => { setInputMoney2(e.target.value) }} pattern="[0-9]*" value={inputMoney2} className={s.inputMoney} placeholder='введите сумму' />


                    </div>
                </div>

                <button className={s.btnclass} onClick={trstFunc}>OK</button>

                <h3>Курс обменика МИГ:</h3>

                <div className={s.mainExchange}>
                    {exchangeStateBuy.objects && exchangeStateBuy.objects.map((elements, index) => {
                        return (
                            <div key={index} className={toggleActiveStyle2(index)} onClick={() => { toggleActive2(index) }}>
                                <p >{elements.currency}</p>
                                <p>Продажа</p>
                                <p >{elements.buy_delta_positive}</p>
                                <p>Покупка</p>
                                <p >{elements.sell_delta_positive}</p>
                            </div>
                        )
                    })}
                </div>
                {/* <button onClick={checkState}>check</button> */}
            </div>

        </div>
    )
}

export default Exchange