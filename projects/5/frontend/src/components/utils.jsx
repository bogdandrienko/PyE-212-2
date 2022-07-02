import React from 'react';

export const GetClearDateTime = (dateTime) => {
    const dateTimeClear = dateTime.slice(0, 19).split('T').join(" ");
    return dateTimeClear;
};
