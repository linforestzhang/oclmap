import React from 'react';
import { useTranslation } from 'react-i18next'
import { useLocation } from 'react-router-dom';
import { styled, useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';
import MuiDrawer from '@mui/material/Drawer';
import MuiAppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import List from '@mui/material/List';
import CssBaseline from '@mui/material/CssBaseline';
import Divider from '@mui/material/Divider';
import MenuIcon from '@mui/icons-material/Menu';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import MenuOpenIcon from '@mui/icons-material/MenuOpen';
import DashboardIcon from '@mui/icons-material/Dashboard';
import FolderOpenIcon from '@mui/icons-material/FolderOutlined';
import BookmarkIcon from '@mui/icons-material/BookmarkBorder';
import Chip from '@mui/material/Chip';
import { COLORS } from '../../common/colors';
import OCLLogo from '../common/OCLLogo';
import SearchInput from '../search/SearchInput';
import './Header.scss';
import HeaderControls from './HeaderControls';
import LeftMenu from './LeftMenu'

const drawerWidth = 258

const openedMixin = theme => ({
  width: drawerWidth,
  overflowX: 'hidden',
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen,
  }),
});

const closedMixin = theme => ({
  overflowX: 'hidden',
  width: `calc(${theme.spacing(7)} + 1px)`,
  [theme.breakpoints.up('sm')]: {
    width: `calc(${theme.spacing(8)} + 1px)`,
  },
  transition: theme.transitions.create('width', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
});

const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'flex-end',
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
}));

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== 'open',
})(({ theme }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(['width', 'margin'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
}));

const Drawer = styled(MuiDrawer, { shouldForwardProp: (prop) => prop !== 'open' })(
  ({ theme, open }) => ({
    width: drawerWidth,
    flexShrink: 0,
    whiteSpace: 'nowrap',
    boxSizing: 'border-box',
    ...(open && {
      ...openedMixin(theme),
      '& .MuiDrawer-paper': openedMixin(theme),
    }),
    ...(!open && {
      ...closedMixin(theme),
      '& .MuiDrawer-paper': closedMixin(theme),
    }),
  }),
);

const Header = props => {
  const { t } = useTranslation()
  /*eslint no-unused-vars: 0*/
  const theme = useTheme();

  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }} style={{backgroundColor: COLORS.surface.n96, color: COLORS.surface.contrastText, boxShadow: 'none'}}>
        <Toolbar style={{paddingRight: '16px'}}>
          <div className='col-xs-12 padding-0 flex-vertical-center'>
            <div className='col-xs-1 padding-0 flex-vertical-center'>
              <OCLLogo />
            </div>
            <div className='col-xs-8' />
            <HeaderControls />
          </div>
        </Toolbar>
      </AppBar>
      <Box component="main" sx={{ flexGrow: 1, paddingTop: 0, paddingBottom: 1.25, paddingLeft: 2, paddingRight: 2 }}>
        <DrawerHeader />
        {
          props.children
        }
      </Box>
    </Box>
  );
}

export default Header;
