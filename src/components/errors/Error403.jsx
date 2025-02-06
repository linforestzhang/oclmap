import React from 'react';
import { useHistory } from 'react-router-dom'
import SvgIcon from '@mui/material/SvgIcon';
import { Trans, useTranslation } from 'react-i18next'
import { BLACK} from '../../common/colors';
import Link from '../common/Link'

const Error403 = () => {
  const history = useHistory()
  const { t } = useTranslation()
  return (
    <div style={{display: 'flex', height: 'calc(100vh - 100px)', alignItems: 'center', justifyContent: 'center', textAlign: 'center', flexDirection: 'column'}}>
      <div className='col-xs-12'>
        <SvgIcon style={{width: "395px", height: "341px", fill: 'none'}} viewBox="0 0 395 341">
          <path d="M144.805 214.456h89.53v1.47h-89.53v-1.47z" fill="#000"/>
          <path d="M188.835 170.424h1.47v89.53h-1.47v-89.53z" fill="#000"/>
          <path d="m190.155 260.395-1.18-.89c.15-.2 14.77-19.89 14.77-44.32s-14.63-44.13-14.77-44.32l1.18-.89c.15.2 15.07 20.27 15.07 45.21s-14.92 45.01-15.07 45.21z" fill="#000"/>
          <path d="M189.575 260.686c-25.09 0-45.5-20.41-45.5-45.5s20.41-45.5 45.5-45.5 45.5 20.41 45.5 45.5-20.41 45.5-45.5 45.5zm0-89.53c-24.28 0-44.03 19.75-44.03 44.03s19.75 44.03 44.03 44.03 44.03-19.75 44.03-44.03-19.75-44.03-44.03-44.03z" fill="#000"/>
          <path d="m189.805 260.655-.47-1.4c.07-.03 7.44-2.55 14.7-9.23 6.68-6.14 14.64-17.17 14.64-34.84s-7.98-28.74-14.68-34.88c-7.26-6.66-14.58-9.16-14.66-9.18l.47-1.4c.31.1 7.7 2.63 15.19 9.5 6.92 6.34 15.16 17.73 15.16 35.97s-8.24 29.62-15.16 35.97c-7.49 6.87-14.87 9.39-15.19 9.5v-.01z" fill="#000"/>
          <path d="M188.985 260.395c-.15-.2-15.07-20.27-15.07-45.21s14.92-45.01 15.07-45.21l1.18.89c-.15.2-14.77 19.89-14.77 44.32s14.63 44.13 14.77 44.32l-1.18.89z" fill="#000"/>
          <path d="M189.335 260.653c-.31-.1-7.7-2.619-15.19-9.499-6.92-6.34-15.16-17.73-15.16-35.97s8.24-29.62 15.16-35.97c7.49-6.87 14.87-9.39 15.19-9.5l.47 1.399c-.07.03-7.44 2.551-14.7 9.231-6.68 6.14-14.64 17.17-14.64 34.84s7.96 28.699 14.64 34.839c7.26 6.68 14.63 9.2 14.7 9.23l-.47 1.4z" fill="#000"/>
          <path d="M229.315 235.915c-4.45-1.91-17.23-6.36-39.74-6.36s-35.29 4.45-39.74 6.36l-.58-1.35c4.53-1.95 17.54-6.48 40.32-6.48s35.79 4.53 40.33 6.48l-.58 1.35h-.01zm-68.89 13.64-.63-1.33c5.06-2.38 14.32-5.22 29.77-5.22s24.61 2.81 29.67 5.17l-.62 1.33c-4.92-2.3-13.95-5.03-29.04-5.03s-24.23 2.76-29.15 5.08zm29.15-47.27c-22.78 0-35.79-4.53-40.32-6.48l.58-1.35c4.45 1.91 17.23 6.36 39.74 6.36s35.29-4.45 39.74-6.36l.58 1.35c-4.53 1.95-17.54 6.48-40.33 6.48h.01zm0-14.92c-15.45 0-24.72-2.84-29.77-5.22l.63-1.33c4.92 2.32 13.97 5.08 29.15 5.08 15.18 0 24.13-2.74 29.04-5.03l.62 1.33c-5.05 2.36-14.3 5.17-29.67 5.17zm-44.76 27.08h89.53v1.47h-89.53v-1.47z" fill="#000"/>
          <path d="M188.835 170.424h1.47v89.53h-1.47v-89.53z" fill="#000"/>
          <path d="m190.155 260.395-1.18-.89c.15-.2 14.77-19.89 14.77-44.32s-14.63-44.13-14.77-44.32l1.18-.89c.15.2 15.07 20.27 15.07 45.21s-14.92 45.01-15.07 45.21z" fill="#000"/>
          <path d="M189.575 260.686c-25.09 0-45.5-20.41-45.5-45.5s20.41-45.5 45.5-45.5 45.5 20.41 45.5 45.5-20.41 45.5-45.5 45.5zm0-89.53c-24.28 0-44.03 19.75-44.03 44.03s19.75 44.03 44.03 44.03 44.03-19.75 44.03-44.03-19.75-44.03-44.03-44.03z" fill="#000"/>
          <path d="m189.805 260.655-.47-1.4c.07-.03 7.44-2.55 14.7-9.23 6.68-6.14 14.64-17.17 14.64-34.84s-7.98-28.74-14.68-34.88c-7.26-6.66-14.58-9.16-14.66-9.18l.47-1.4c.31.1 7.7 2.63 15.19 9.5 6.92 6.34 15.16 17.73 15.16 35.97s-8.24 29.62-15.16 35.97c-7.49 6.87-14.87 9.39-15.19 9.5v-.01z" fill="#000"/>
          <path d="M188.985 260.395c-.15-.2-15.07-20.27-15.07-45.21s14.92-45.01 15.07-45.21l1.18.89c-.15.2-14.77 19.89-14.77 44.32s14.63 44.13 14.77 44.32l-1.18.89z" fill="#000"/>
          <path d="M189.335 260.653c-.31-.1-7.7-2.619-15.19-9.499-6.92-6.34-15.16-17.73-15.16-35.97s8.24-29.62 15.16-35.97c7.49-6.87 14.87-9.39 15.19-9.5l.47 1.399c-.07.03-7.44 2.551-14.7 9.231-6.68 6.14-14.64 17.17-14.64 34.84s7.96 28.699 14.64 34.839c7.26 6.68 14.63 9.2 14.7 9.23l-.47 1.4z" fill="#000"/>
          <path d="M252.705 11.405H80.665c-8.765 0-15.87 7.105-15.87 15.87v172.04c0 8.765 7.105 15.87 15.87 15.87h172.04c8.765 0 15.87-7.105 15.87-15.87V27.275c0-8.765-7.105-15.87-15.87-15.87z" fill="#EBE7EC" stroke="#000" strokeWidth="1.5" strokeMiterlimit="10"/>
          <g clipPath="url(#4tcwtv2j1a)" fill="#fff">
            <path d="M118.122 144.954c15.514 0 28.091-12.497 28.091-27.914 0-15.416-12.577-27.914-28.091-27.914-15.515 0-28.092 12.498-28.092 27.914 0 15.417 12.577 27.914 28.092 27.914zM182.12 144.954c-15.515 0-28.092-12.498-28.092-27.914 0-15.416 12.577-27.914 28.092-27.914M205.715 116.914c7.758 0 14.046-6.249 14.046-13.957 0-7.708-6.288-13.957-14.046-13.957-7.757 0-14.046 6.249-14.046 13.957 0 7.708 6.289 13.957 14.046 13.957zM205.715 146c7.758 0 14.046-6.249 14.046-13.957 0-7.708-6.288-13.957-14.046-13.957-7.757 0-14.046 6.249-14.046 13.957 0 7.708 6.289 13.957 14.046 13.957zM234.984 146c7.758 0 14.046-6.249 14.046-13.957 0-7.708-6.288-13.957-14.046-13.957-7.757 0-14.046 6.249-14.046 13.957 0 7.708 6.289 13.957 14.046 13.957z"/>
          </g>
          <path d="M377.775 136.085h-173.07c-8.765 0-15.87 7.105-15.87 15.87v172.04c0 8.764 7.105 15.87 15.87 15.87h173.07c8.765 0 15.87-7.106 15.87-15.87v-172.04c0-8.765-7.105-15.87-15.87-15.87z" fill="#4836FF" stroke="#fff" strokeWidth="1.5" strokeMiterlimit="10"/>
          <path d="M80.665 11.405h172.04c8.76 0 15.87 7.11 15.87 15.87v15.87H64.795v-15.87c0-8.76 7.11-15.87 15.87-15.87z" fill="#E5E1E6" stroke="#1D1D1B" strokeWidth="1.5" strokeMiterlimit="10"/>
          <path d="M204.705 136.085h172.77c8.76 0 15.87 7.11 15.87 15.87v15.87h-204.52v-15.87c0-8.76 7.11-15.87 15.87-15.87h.01z" fill="#4836FF" stroke="#fff" strokeWidth="1.5" strokeMiterlimit="10"/>
          <path d="M209.965 157.693a5.74 5.74 0 1 0 0-11.479 5.74 5.74 0 1 0 0 11.479zM228.035 157.693a5.74 5.74 0 1 0 0-11.479 5.74 5.74 0 1 0 0 11.479zM246.105 157.693a5.74 5.74 0 1 0 0-11.479 5.74 5.74 0 1 0 0 11.479z" fill="#fff"/>
          <path d="M84.245 34.315a5.74 5.74 0 1 0 0-11.48 5.74 5.74 0 0 0 0 11.48zM102.315 34.315a5.74 5.74 0 1 0 0-11.48 5.74 5.74 0 0 0 0 11.48zM120.395 34.315a5.74 5.74 0 1 0 0-11.48 5.74 5.74 0 0 0 0 11.48z" fill="#000"/>
          <path d="M361.455 292.104h-141.07a4.68 4.68 0 0 0-4.68 4.68v11.35a4.68 4.68 0 0 0 4.68 4.68h141.07a4.68 4.68 0 0 0 4.68-4.68v-11.35a4.68 4.68 0 0 0-4.68-4.68z" fill="#fff" stroke="#4836FF" strokeWidth="1.5" strokeMiterlimit="10"/>
          <path d="M359.798 294.835H221.391c-1.483 0-2.686.926-2.686 2.07v11.11c0 1.143 1.203 2.07 2.686 2.07h138.407c1.484 0 2.687-.927 2.687-2.07v-11.11c0-1.144-1.203-2.07-2.687-2.07z" fill="#4836FF" stroke="#4836FF" strokeWidth=".75" strokeMiterlimit="10"/>
          <path d="M204.225 27.276h83.81c3.62 0 6.55 2.93 6.55 6.55v41.76c0 3.62 2.93 6.55 6.55 6.55h38.81c3.62 0 6.55 2.93 6.55 6.55v47.38" stroke="#000" strokeWidth="1.5" strokeMiterlimit="10"/>
          <path d="M202.675 29.825a2.55 2.55 0 1 0 0-5.1 2.55 2.55 0 0 0 0 5.1z" fill="#000"/>
          <path d="M346.515 138.085v27.08" stroke="#4836FF" strokeLinecap="round" strokeLinejoin="round"/>
          <path d="M346.515 168.956v39.5" stroke="#fff" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
          <path opacity=".6" d="m355.675.135 1.41 3.66 3.66 1.41-3.66 1.41-1.41 3.66-1.41-3.66-3.66-1.41 3.66-1.41 1.41-3.66z" fill="#fff"/>
          <path d="M346.515 208.454s0-16.78-15.26-16.78z" fill="#4836FF"/>
          <path d="M346.515 208.454s0-16.78-15.26-16.78" stroke="#fff" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
          <path d="M346.515 208.454s0-16.78 15.26-16.78z" fill="#4836FF"/>
          <path d="M346.515 208.454s0-16.78 15.26-16.78" stroke="#fff" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
          <path opacity=".6" d="m5.425 199.444 1.41 3.66 3.66 1.41-3.66 1.41-1.41 3.66-1.41-3.66-3.66-1.41 3.66-1.41 1.41-3.66z" fill="#fff"/>
          <path d="M269.626 260.38h-5.55V270h-10.138v-9.62H229.37v-8.954l21.978-25.826h12.728v25.826h5.55v8.954zm-20.794-8.954h5.106V235.59l-.148-.074-13.024 16.058c3.182-.148 5.994-.148 8.066-.148zm42.629-17.316c-6.364 0-9.916 5.18-9.916 13.542s3.552 13.838 9.768 13.838c6.438 0 9.99-5.476 9.99-13.838 0-8.362-3.552-13.542-9.842-13.542zm0-9.546c12.062 0 20.498 8.066 20.498 23.088s-8.14 23.384-20.498 23.384c-12.432 0-20.498-8.362-20.498-23.384s8.51-23.088 20.498-23.088zm41.562 46.176c-11.988 0-18.648-5.18-19.462-16.206l10.434-.814c.666 4.81 2.442 7.77 9.324 7.77 4.81 0 7.326-1.924 7.326-5.106s-1.554-4.736-7.178-4.736h-7.104v-7.844h7.104c3.922 0 6.216-1.258 6.216-4.662 0-3.552-2.294-5.032-6.882-5.032-5.772 0-7.4 2.59-7.992 7.03l-10.064-.814c1.036-9.472 6.512-15.466 17.982-15.466 11.692 0 16.798 4.218 16.798 11.914 0 5.698-3.108 8.954-8.732 10.508v.148c7.992 1.036 10.508 4.218 10.508 10.286 0 7.548-5.328 13.024-18.278 13.024z" fill="#fff"/>
          <defs>
            <clipPath id="4tcwtv2j1a">
              <path fill="#fff" transform="translate(90.03 89)" d="M0 0h159v57H0z"/>
            </clipPath>
          </defs>
        </SvgIcon>
      </div>
      <div className='col-xs-12'>
        <p style={{color: '#000', fontSize: '24px', margin: '16px 0'}}>
          {t('errors.403')}
        </p>
      </div>
      <div className='col-xs-12'>
        <p style={{color: BLACK, fontSize: '16px', margin: 0, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
          <Trans
            i18nKey='common.go_back_or_to_your_dashboard'
            components={[
              <Link key='back' sx={{minWidth: 'auto', fontSize: '16px', padding: '0 4px'}} label={t('common.back')} onClick={() => history.goBack()} />,
              <Link key='dashboard' sx={{minWidth: 'auto', fontSize: '16px', paddingLeft: '4px'}} label={t('dashboard.name')} href='/#/' />,
            ]}
          />
        </p>
      </div>
    </div>
  )
}

export default Error403;
