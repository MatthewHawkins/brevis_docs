/** @jsxImportSource @emotion/react */
import { css } from '@emotion/react'
import Link from '@docusaurus/Link'

import React from 'react'

export default function FrontPageLink( {imgPath, description, path} ) {
  
  const mainStyles = css`
    display: flex;
    flex-direction: column;
    align-items: center;
  `
  
  return (
    <Link css={mainStyles} to={path}>
      <img src={imgPath}></img>
      <div>{description}</div>
    </Link>
  )
}
