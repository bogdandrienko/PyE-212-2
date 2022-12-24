import React from 'react'
import s from './Menu.module.css';
import { NavLink } from 'react-router-dom';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {faYoutube} from '@fortawesome/free-brands-svg-icons'
import {faBars,faUser, faUsers, faDollar, faComments, faFile } from '@fortawesome/free-solid-svg-icons'
// import {faBlogger} from '@fortawesome/free-regular-svg-icons'

import { useNavigate } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux'

import { logout } from '../../redux/auth-reducer';



const Menu = () => {
  const store = useSelector(state => state.authReducerR);
  const dispatch = useDispatch()
  const navigate = useNavigate();

//     const arr = [fa42Group, fa500px, faAccessibleIcon, faAccusoft, faAdn, faAdversal, faAffiliatetheme, faAirbnb, faAlgolia, faAlipay, faAmazon, faAmazonPay, faAmilia, faAndroid, faAngellist, faAngrycreative, faAngular, faAppStore, faAppStoreIos, faApper, faApple, faApplePay, faArtstation, faAsymmetrik, faAtlassian, faAudible, faAutoprefixer, faAvianex, faAviato, faAws, faBandcamp, faBattleNet, faBehance, faBehanceSquare, faBilibili, faBimobject, faBitbucket, faBitcoin, faBity, faBlackTie, faBlackberry, faBlogger, faBloggerB, faBluetooth, faBluetoothB, faBootstrap, faBots, faBtc, faBuffer, faBuromobelexperte, faBuyNLarge, faBuysellads, faCanadianMapleLeaf, faCcAmazonPay, faCcAmex, faCcApplePay, faCcDinersClub, faCcDiscover, faCcJcb, faCcMastercard, faCcPaypal, faCcStripe, faCcVisa, faCentercode, faCentos, faChrome, faChromecast, faCloudflare, faCloudscale, faCloudsmith, faCloudversify, faCmplid, faCodepen, faCodiepie, faConfluence, faConnectdevelop, faContao, faCottonBureau, faCpanel, faCreativeCommons, faCreativeCommonsBy, faCreativeCommonsNc, faCreativeCommonsNcEu, faCreativeCommonsNcJp, faCreativeCommonsNd, faCreativeCommonsPd, faCreativeCommonsPdAlt, faCreativeCommonsRemix, faCreativeCommonsSa, faCreativeCommonsSampling, faCreativeCommonsSamplingPlus, faCreativeCommonsShare, faCreativeCommonsZero, faCriticalRole, faCss3, faCss3Alt, faCuttlefish, faDAndD, faDAndDBeyond, faDailymotion, faDashcube, faDeezer, faDelicious, faDeploydog, faDeskpro, faDev, faDeviantart, faDhl, faDiaspora, faDigg, faDigitalOcean, faDiscord, faDiscourse, faDochub, faDocker, faDraft2digital, faDribbble, faDribbbleSquare, faDropbox, faDrupal, faDyalog, faEarlybirds, faEbay, faEdge, faEdgeLegacy, faElementor, faEllo, faEmber, faEmpire, faEnvira, faErlang, faEthereum, faEtsy, faEvernote, faExpeditedssl, faFacebook, faFacebookF, faFacebookMessenger, faFacebookSquare, faFantasyFlightGames, faFedex, faFedora, faFigma, faFirefox, faFirefoxBrowser, faFirstOrder, faFirstOrderAlt, faFirstdraft, faFlickr, faFlipboard, faFly, faFontAwesome, faFontAwesomeAlt, faFontAwesomeFlag, faFontAwesomeLogoFull, faFonticons, faFonticonsFi, faFortAwesome, faFortAwesomeAlt, faForumbee, faFoursquare, faFreeCodeCamp, faFreebsd, faFulcrum, faGalacticRepublic, faGalacticSenate, faGetPocket, faGg, faGgCircle, faGit, faGitAlt, faGitSquare, faGithub, faGithubAlt, faGithubSquare, faGitkraken, faGitlab, faGitlabSquare, faGitter, faGlide, faGlideG, faGofore, faGolang, faGoodreads, faGoodreadsG, faGoogle, faGoogleDrive, faGooglePay, faGooglePlay, faGooglePlus, faGooglePlusG, faGooglePlusSquare, faGoogleWallet, faGratipay, faGrav, faGripfire, faGrunt, faGuilded, faGulp, faHackerNews, faHackerNewsSquare, faHackerrank, faHashnode, faHips, faHireAHelper, faHive, faHooli, faHornbill, faHotjar, faHouzz, faHtml5, faHubspot, faIdeal, faImdb, faInnosoft, faInstagram, faInstagramSquare, faInstalod, faIntercom, faInternetExplorer, faInvision, faIoxhost, faItchIo, faItunes, faItunesNote, faJava, faJediOrder, faJenkins, faJira, faJoget, faJoomla, faJs, faJsSquare, faJsfiddle, faKaggle, faKeybase, faKeycdn, faKickstarter, faKickstarterK, faKorvue, faLaravel, faLastfm, faLastfmSquare, faLeanpub, faLess, faLine, faLinkedin, faLinkedinIn, faLinode, faLinux, faLyft, faMagento, faMailchimp, faMandalorian, faMarkdown, faMastodon, faMaxcdn, faMdb, faMedapps, faMedium, faMediumM, faMedrt, faMeetup, faMegaport, faMendeley, faMeta, faMicroblog, faMicrosoft, faMix, faMixcloud, faMixer, faMizuni, faModx, faMonero, faNapster, faNeos, faNfcDirectional, faNfcSymbol, faNimblr, faNode, faNodeJs, faNpm, faNs8, faNutritionix, faOctopusDeploy, faOdnoklassniki, faOdnoklassnikiSquare, faOldRepublic, faOpencart, faOpenid, faOpera, faOptinMonster, faOrcid, faOsi, faPadlet, faPage4, faPagelines, faPalfed, faPatreon, faPaypal, faPerbyte, faPeriscope, faPhabricator, faPhoenixFramework, faPhoenixSquadron, faPhp, faPiedPiper, faPiedPiperAlt, faPiedPiperHat, faPiedPiperPp, faPiedPiperSquare, faPinterest, faPinterestP, faPinterestSquare, faPix, faPlaystation, faProductHunt, faPushed, faPython, faQq, faQuinscape, faQuora, faRProject, faRaspberryPi, faRavelry, faReact, faReacteurope, faReadme, faRebel, faRedRiver, faReddit, faRedditAlien, faRedditSquare, faRedhat, faRendact, faRenren, faReplyd, faResearchgate, faResolving, faRev, faRocketchat, faRockrms, faRust, faSafari, faSalesforce, faSass, faSchlix, faScreenpal, faScribd, faSearchengin, faSellcast, faSellsy, faServicestack, faShirtsinbulk, faShopify, faShopware, faSimplybuilt, faSistrix, faSith, faSitrox, faSketch, faSkyatlas, faSkype, faSlack, faSlackHash, faSlideshare, faSnapchat, faSnapchatGhost, faSnapchatSquare, faSoundcloud, faSourcetree, faSpaceAwesome, faSpeakap, faSpeakerDeck, faSpotify, faSquareBehance, faSquareDribbble, faSquareFacebook, faSquareFontAwesome, faSquareFontAwesomeStroke, faSquareGit, faSquareGithub, faSquareGitlab, faSquareGooglePlus, faSquareHackerNews, faSquareInstagram, faSquareJs, faSquareLastfm, faSquareOdnoklassniki, faSquarePiedPiper, faSquarePinterest, faSquareReddit, faSquareSnapchat, faSquareSteam, faSquareTumblr, faSquareTwitter, faSquareViadeo, faSquareVimeo, faSquareWhatsapp, faSquareXing, faSquareYoutube, faSquarespace, faStackExchange, faStackOverflow, faStackpath, faStaylinked, faSteam, faSteamSquare, faSteamSymbol, faStickerMule, faStrava, faStripe, faStripeS, faStudiovinari, faStumbleupon, faStumbleuponCircle, faSuperpowers, faSupple, faSuse, faSwift, faSymfony, faTeamspeak, faTelegram, faTelegramPlane, faTencentWeibo, faTheRedYeti, faThemeco, faThemeisle, faThinkPeaks, faTiktok, faTradeFederation, faTrello, faTumblr, faTumblrSquare, faTwitch, faTwitter, faTwitterSquare, faTypo3, faUber, faUbuntu, faUikit, faUmbraco, faUncharted, faUniregistry, faUnity, faUnsplash, faUntappd, faUps, faUsb, faUsps, faUssunnah, faVaadin, faViacoin, faViadeo, faViadeoSquare, faViber, faVimeo, faVimeoSquare, faVimeoV, faVine, faVk, faVnv, faVuejs, faWatchmanMonitoring, faWaze, faWeebly, faWeibo, faWeixin, faWhatsapp, faWhatsappSquare, faWhmcs, faWikipediaW, faWindows, faWirsindhandwerk, faWix, faWizardsOfTheCoast, faWodu, faWolfPackBattalion, faWordpress, faWordpressSimple, faWpbeginner, faWpexplorer, faWpforms, faWpressr, faWsh, faXbox, faXing, faXingSquare, faYCombinator, faYahoo, faYammer, faYandex, faYandexInternational, faYarn, faYelp, faYoast, faYoutube, faYoutubeSquare, faZhihu, fab, prefix
// ]

const exit = () => {
  console.log("exit");
  logout(dispatch)
  navigate('/login')

}


  return ( 
    <div className={s.wrapper}>
        
    
    <div className={ `${s.menuMain} ${s.sidebar}` }>
        
        <div className={`${s.singleCol} ${s.socialMediaIconsWhite}`}>      
            
           <NavLink to="/"> <FontAwesomeIcon icon={faBars} /> <span className={s.spanList}>Главная</span> </NavLink>   
            
        </div>

        <div className={`${s.singleCol} ${s.socialMediaIconsWhite}`}>            
            <NavLink to="/profile"><FontAwesomeIcon icon={faUser} /> <span className={s.spanList}>Профиль</span> </NavLink>           
        </div> 
        <div className={`${s.singleCol} ${s.socialMediaIconsWhite}`}>            
            <NavLink to="/video"><FontAwesomeIcon icon={faYoutube} /> <span className={s.spanList}>Видео</span> </NavLink>           
        </div> 
        <div className={`${s.singleCol} ${s.socialMediaIconsWhite}`}>            
            <NavLink to="/users"><FontAwesomeIcon icon={faUsers} /> <span className={s.spanList}>Пользователи</span> </NavLink>           
        </div> 

        <div className={`${s.singleCol} ${s.socialMediaIconsWhite}`}>            
            <NavLink to="/exchange"><FontAwesomeIcon icon={faDollar} /> <span className={s.spanList}>Обменик2</span> </NavLink>           
        </div> 

        <div className={`${s.singleCol} ${s.socialMediaIconsWhite}`}>            
            <NavLink to="/posts"><FontAwesomeIcon icon={faFile} /> <span className={s.spanList}>Посты</span> </NavLink>           
        </div> 

        <div className={`${s.singleCol} ${s.socialMediaIconsWhite}`}>  
               <a href='/api/frontpage' className="nav-link nav-custom2" > <FontAwesomeIcon icon={faComments} /> Чат</a>
         </div> 

        <div className={`${s.singleCol} ${s.socialMediaIconsWhite}`}>            
          {store.isAuth && <button onClick={exit}>выйти</button>}     
        </div> 

         

        
        
        
    </div> 
  
        
    </div>
  )
}

export default Menu






// arr.map(item => {
//     return(
//         <a href=''>
//             <FontAwesomeIcon icon={item} />
//          </a>
//     )
    
// })}