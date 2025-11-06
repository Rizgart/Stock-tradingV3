const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  toggleTheme: () => ipcRenderer.invoke('toggle-theme')
});
