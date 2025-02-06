import React from 'react';
import { ListItem, ListItemText } from '@mui/material';
import RepoChip from './RepoChip'

const RepoListItem = ({ option, listItemProps, style, repoChipProps }) => {
  return (
    <ListItem
      {...listItemProps}
      alignItems="flex-start"
      sx={{alignItems: 'flex-start', ...style}}
    >
      <ListItemText primary={<RepoChip noLink filled repo={option} {...repoChipProps} />} />
    </ListItem>

  )
}

export default RepoListItem;
