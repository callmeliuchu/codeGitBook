from bs4 import BeautifulSoup
colors = """
                          <tr>
                            <td height="30" width="30" bgcolor="#ffffff"></td>
                            <td>#FFFFFF</td>
                            <td height="30" width="30" bgcolor="#fffff0"></td>
                            <td>#FFFFF0</td>
                            <td height="30" width="30" bgcolor="#ffffe0"></td>
                            <td>#FFFFE0</td>
                            <td height="30" width="30" bgcolor="#ffff00"></td>
                            <td>#FFFF00</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#fffafa"></td>
                            <td>#FFFAFA</td>
                            <td height="30" width="30" bgcolor="#fffaf0"></td>
                            <td>#FFFAF0</td>
                            <td height="30" width="30" bgcolor="#fffacd"></td>
                            <td>#FFFACD</td>
                            <td height="30" width="30" bgcolor="#fff8dc"></td>
                            <td>#FFF8DC</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#fff68f"></td>
                            <td>#FFF68F</td>
                            <td height="30" width="30" bgcolor="#fff5ee"></td>
                            <td>#FFF5EE</td>
                            <td height="30" width="30" bgcolor="#fff0f5"></td>
                            <td>#FFF0F5</td>
                            <td height="30" width="30" bgcolor="#ffefdb"></td>
                            <td>#FFEFDB</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ffefd5"></td>
                            <td>#FFEFD5</td>
                            <td height="30" width="30" bgcolor="#ffec8b"></td>
                            <td>#FFEC8B</td>
                            <td height="30" width="30" bgcolor="#ffebcd"></td>
                            <td>#FFEBCD</td>
                            <td height="30" width="30" bgcolor="#ffe7ba"></td>
                            <td>#FFE7BA</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ffe4e1"></td>
                            <td>#FFE4E1</td>
                            <td height="30" width="30" bgcolor="#ffe4c4"></td>
                            <td>#FFE4C4</td>
                            <td height="30" width="30" bgcolor="#ffe4b5"></td>
                            <td>#FFE4B5</td>
                            <td height="30" width="30" bgcolor="#ffe1ff"></td>
                            <td>#FFE1FF</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ffdead"></td>
                            <td>#FFDEAD</td>
                            <td height="30" width="30" bgcolor="#ffdab9"></td>
                            <td>#FFDAB9</td>
                            <td height="30" width="30" bgcolor="#ffd700"></td>
                            <td>#FFD700</td>
                            <td height="30" width="30" bgcolor="#ffd39b"></td>
                            <td>#FFD39B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ffc1c1"></td>
                            <td>#FFC1C1</td>
                            <td height="30" width="30" bgcolor="#ffc125"></td>
                            <td>#FFC125</td>
                            <td height="30" width="30" bgcolor="#ffc0cb"></td>
                            <td>#FFC0CB</td>
                            <td height="30" width="30" bgcolor="#ffbbff"></td>
                            <td>#FFBBFF</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ffb90f"></td>
                            <td>#FFB90F</td>
                            <td height="30" width="30" bgcolor="#ffb6c1"></td>
                            <td>#FFB6C1</td>
                            <td height="30" width="30" bgcolor="#ffb5c5"></td>
                            <td>#FFB5C5</td>
                            <td height="30" width="30" bgcolor="#ffaeb9"></td>
                            <td>#FFAEB9</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ffa54f"></td>
                            <td>#FFA54F</td>
                            <td height="30" width="30" bgcolor="#ffa500"></td>
                            <td>#FFA500</td>
                            <td height="30" width="30" bgcolor="#ffa07a"></td>
                            <td>#FFA07A</td>
                            <td height="30" width="30" bgcolor="#ff8c69"></td>
                            <td>#FF8C69</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ff8c00"></td>
                            <td>#FF8C00</td>
                            <td height="30" width="30" bgcolor="#ff83fa"></td>
                            <td>#FF83FA</td>
                            <td height="30" width="30" bgcolor="#ff82ab"></td>
                            <td>#FF82AB</td>
                            <td height="30" width="30" bgcolor="#ff8247"></td>
                            <td>#FF8247</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ff7f50"></td>
                            <td>#FF7F50</td>
                            <td height="30" width="30" bgcolor="#ff7f24"></td>
                            <td>#FF7F24</td>
                            <td height="30" width="30" bgcolor="#ff7f00"></td>
                            <td>#FF7F00</td>
                            <td height="30" width="30" bgcolor="#ff7256"></td>
                            <td>#FF7256</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ff6eb4"></td>
                            <td>#FF6EB4</td>
                            <td height="30" width="30" bgcolor="#ff6a6a"></td>
                            <td>#FF6A6A</td>
                            <td height="30" width="30" bgcolor="#ff69b4"></td>
                            <td>#FF69B4</td>
                            <td height="30" width="30" bgcolor="#ff6347"></td>
                            <td>#FF6347</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ff4500"></td>
                            <td>#FF4500</td>
                            <td height="30" width="30" bgcolor="#ff4040"></td>
                            <td>#FF4040</td>
                            <td height="30" width="30" bgcolor="#ff3e96"></td>
                            <td>#FF3E96</td>
                            <td height="30" width="30" bgcolor="#ff34b3"></td>
                            <td>#FF34B3</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ff3030"></td>
                            <td>#FF3030</td>
                            <td height="30" width="30" bgcolor="#ff1493"></td>
                            <td>#FF1493</td>
                            <td height="30" width="30" bgcolor="#ff00ff"></td>
                            <td>#FF00FF</td>
                            <td height="30" width="30" bgcolor="#ff0000"></td>
                            <td>#FF0000</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#fdf5e6"></td>
                            <td>#FDF5E6</td>
                            <td height="30" width="30" bgcolor="#fcfcfc"></td>
                            <td>#FCFCFC</td>
                            <td height="30" width="30" bgcolor="#fafafa"></td>
                            <td>#FAFAFA</td>
                            <td height="30" width="30" bgcolor="#fafad2"></td>
                            <td>#FAFAD2</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#faf0e6"></td>
                            <td>#FAF0E6</td>
                            <td height="30" width="30" bgcolor="#faebd7"></td>
                            <td>#FAEBD7</td>
                            <td height="30" width="30" bgcolor="#fa8072"></td>
                            <td>#FA8072</td>
                            <td height="30" width="30" bgcolor="#f8f8ff"></td>
                            <td>#F8F8FF</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#f7f7f7"></td>
                            <td>#F7F7F7</td>
                            <td height="30" width="30" bgcolor="#f5fffa"></td>
                            <td>#F5FFFA</td>
                            <td height="30" width="30" bgcolor="#f5f5f5"></td>
                            <td>#F5F5F5</td>
                            <td height="30" width="30" bgcolor="#f5f5dc"></td>
                            <td>#F5F5DC</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#f5deb3"></td>
                            <td>#F5DEB3</td>
                            <td height="30" width="30" bgcolor="#f4f4f4"></td>
                            <td>#F4F4F4</td>
                            <td height="30" width="30" bgcolor="#f4a460"></td>
                            <td>#F4A460</td>
                            <td height="30" width="30" bgcolor="#f2f2f2"></td>
                            <td>#F2F2F2</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#f0ffff"></td>
                            <td>#F0FFFF</td>
                            <td height="30" width="30" bgcolor="#f0fff0"></td>
                            <td>#F0FFF0</td>
                            <td height="30" width="30" bgcolor="#f0f8ff"></td>
                            <td>#F0F8FF</td>
                            <td height="30" width="30" bgcolor="#f0f0f0"></td>
                            <td>#F0F0F0</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#f0e68c"></td>
                            <td>#F0E68C</td>
                            <td height="30" width="30" bgcolor="#f08080"></td>
                            <td>#F08080</td>
                            <td height="30" width="30" bgcolor="#eeeee0"></td>
                            <td>#EEEEE0</td>
                            <td height="30" width="30" bgcolor="#eeeed1"></td>
                            <td>#EEEED1</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#eeee00"></td>
                            <td>#EEEE00</td>
                            <td height="30" width="30" bgcolor="#eee9e9"></td>
                            <td>#EEE9E9</td>
                            <td height="30" width="30" bgcolor="#eee9bf"></td>
                            <td>#EEE9BF</td>
                            <td height="30" width="30" bgcolor="#eee8cd"></td>
                            <td>#EEE8CD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#eee8aa"></td>
                            <td>#EEE8AA</td>
                            <td height="30" width="30" bgcolor="#eee685"></td>
                            <td>#EEE685</td>
                            <td height="30" width="30" bgcolor="#eee5de"></td>
                            <td>#EEE5DE</td>
                            <td height="30" width="30" bgcolor="#eee0e5"></td>
                            <td>#EEE0E5</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#eedfcc"></td>
                            <td>#EEDFCC</td>
                            <td height="30" width="30" bgcolor="#eedc82"></td>
                            <td>#EEDC82</td>
                            <td height="30" width="30" bgcolor="#eed8ae"></td>
                            <td>#EED8AE</td>
                            <td height="30" width="30" bgcolor="#eed5d2"></td>
                            <td>#EED5D2</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#eed5b7"></td>
                            <td>#EED5B7</td>
                            <td height="30" width="30" bgcolor="#eed2ee"></td>
                            <td>#EED2EE</td>
                            <td height="30" width="30" bgcolor="#eecfa1"></td>
                            <td>#EECFA1</td>
                            <td height="30" width="30" bgcolor="#eecbad"></td>
                            <td>#EECBAD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#eec900"></td>
                            <td>#EEC900</td>
                            <td height="30" width="30" bgcolor="#eec591"></td>
                            <td>#EEC591</td>
                            <td height="30" width="30" bgcolor="#eeb4b4"></td>
                            <td>#EEB4B4</td>
                            <td height="30" width="30" bgcolor="#eeb422"></td>
                            <td>#EEB422</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#eeaeee"></td>
                            <td>#EEAEEE</td>
                            <td height="30" width="30" bgcolor="#eead0e"></td>
                            <td>#EEAD0E</td>
                            <td height="30" width="30" bgcolor="#eea9b8"></td>
                            <td>#EEA9B8</td>
                            <td height="30" width="30" bgcolor="#eea2ad"></td>
                            <td>#EEA2AD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ee9a49"></td>
                            <td>#EE9A49</td>
                            <td height="30" width="30" bgcolor="#ee9a00"></td>
                            <td>#EE9A00</td>
                            <td height="30" width="30" bgcolor="#ee9572"></td>
                            <td>#EE9572</td>
                            <td height="30" width="30" bgcolor="#ee82ee"></td>
                            <td>#EE82EE</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ee8262"></td>
                            <td>#EE8262</td>
                            <td height="30" width="30" bgcolor="#ee7ae9"></td>
                            <td>#EE7AE9</td>
                            <td height="30" width="30" bgcolor="#ee799f"></td>
                            <td>#EE799F</td>
                            <td height="30" width="30" bgcolor="#ee7942"></td>
                            <td>#EE7942</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ee7621"></td>
                            <td>#EE7621</td>
                            <td height="30" width="30" bgcolor="#ee7600"></td>
                            <td>#EE7600</td>
                            <td height="30" width="30" bgcolor="#ee6aa7"></td>
                            <td>#EE6AA7</td>
                            <td height="30" width="30" bgcolor="#ee6a50"></td>
                            <td>#EE6A50</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ee6363"></td>
                            <td>#EE6363</td>
                            <td height="30" width="30" bgcolor="#ee5c42"></td>
                            <td>#EE5C42</td>
                            <td height="30" width="30" bgcolor="#ee4000"></td>
                            <td>#EE4000</td>
                            <td height="30" width="30" bgcolor="#ee3b3b"></td>
                            <td>#EE3B3B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ee3a8c"></td>
                            <td>#EE3A8C</td>
                            <td height="30" width="30" bgcolor="#ee30a7"></td>
                            <td>#EE30A7</td>
                            <td height="30" width="30" bgcolor="#ee2c2c"></td>
                            <td>#EE2C2C</td>
                            <td height="30" width="30" bgcolor="#ee1289"></td>
                            <td>#EE1289</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#ee00ee"></td>
                            <td>#EE00EE</td>
                            <td height="30" width="30" bgcolor="#ee0000"></td>
                            <td>#EE0000</td>
                            <td height="30" width="30" bgcolor="#ededed"></td>
                            <td>#EDEDED</td>
                            <td height="30" width="30" bgcolor="#ebebeb"></td>
                            <td>#EBEBEB</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#eaeaea"></td>
                            <td>#EAEAEA</td>
                            <td height="30" width="30" bgcolor="#e9967a"></td>
                            <td>#E9967A</td>
                            <td height="30" width="30" bgcolor="#e8e8e8"></td>
                            <td>#E8E8E8</td>
                            <td height="30" width="30" bgcolor="#e6e6fa"></td>
                            <td>#E6E6FA</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#e5e5e5"></td>
                            <td>#E5E5E5</td>
                            <td height="30" width="30" bgcolor="#e3e3e3"></td>
                            <td>#E3E3E3</td>
                            <td height="30" width="30" bgcolor="#e0ffff"></td>
                            <td>#E0FFFF</td>
                            <td height="30" width="30" bgcolor="#e0eeee"></td>
                            <td>#E0EEEE</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#e0eee0"></td>
                            <td>#E0EEE0</td>
                            <td height="30" width="30" bgcolor="#e0e0e0"></td>
                            <td>#E0E0E0</td>
                            <td height="30" width="30" bgcolor="#e066ff"></td>
                            <td>#E066FF</td>
                            <td height="30" width="30" bgcolor="#dedede"></td>
                            <td>#DEDEDE</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#deb887"></td>
                            <td>#DEB887</td>
                            <td height="30" width="30" bgcolor="#dda0dd"></td>
                            <td>#DDA0DD</td>
                            <td height="30" width="30" bgcolor="#dcdcdc"></td>
                            <td>#DCDCDC</td>
                            <td height="30" width="30" bgcolor="#dc143c"></td>
                            <td>#DC143C</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#dbdbdb"></td>
                            <td>#DBDBDB</td>
                            <td height="30" width="30" bgcolor="#db7093"></td>
                            <td>#DB7093</td>
                            <td height="30" width="30" bgcolor="#daa520"></td>
                            <td>#DAA520</td>
                            <td height="30" width="30" bgcolor="#da70d6"></td>
                            <td>#DA70D6</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#d9d9d9"></td>
                            <td>#D9D9D9</td>
                            <td height="30" width="30" bgcolor="#d8bfd8"></td>
                            <td>#D8BFD8</td>
                            <td height="30" width="30" bgcolor="#d6d6d6"></td>
                            <td>#D6D6D6</td>
                            <td height="30" width="30" bgcolor="#d4d4d4"></td>
                            <td>#D4D4D4</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#d3d3d3"></td>
                            <td>#D3D3D3</td>
                            <td height="30" width="30" bgcolor="#d2b48c"></td>
                            <td>#D2B48C</td>
                            <td height="30" width="30" bgcolor="#d2691e"></td>
                            <td>#D2691E</td>
                            <td height="30" width="30" bgcolor="#d1eeee"></td>
                            <td>#D1EEEE</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#d1d1d1"></td>
                            <td>#D1D1D1</td>
                            <td height="30" width="30" bgcolor="#d15fee"></td>
                            <td>#D15FEE</td>
                            <td height="30" width="30" bgcolor="#d02090"></td>
                            <td>#D02090</td>
                            <td height="30" width="30" bgcolor="#cfcfcf"></td>
                            <td>#CFCFCF</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cdcdc1"></td>
                            <td>#CDCDC1</td>
                            <td height="30" width="30" bgcolor="#cdcdb4"></td>
                            <td>#CDCDB4</td>
                            <td height="30" width="30" bgcolor="#cdcd00"></td>
                            <td>#CDCD00</td>
                            <td height="30" width="30" bgcolor="#cdc9c9"></td>
                            <td>#CDC9C9</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cdc9a5"></td>
                            <td>#CDC9A5</td>
                            <td height="30" width="30" bgcolor="#cdc8b1"></td>
                            <td>#CDC8B1</td>
                            <td height="30" width="30" bgcolor="#cdc673"></td>
                            <td>#CDC673</td>
                            <td height="30" width="30" bgcolor="#cdc5bf"></td>
                            <td>#CDC5BF</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cdc1c5"></td>
                            <td>#CDC1C5</td>
                            <td height="30" width="30" bgcolor="#cdc0b0"></td>
                            <td>#CDC0B0</td>
                            <td height="30" width="30" bgcolor="#cdbe70"></td>
                            <td>#CDBE70</td>
                            <td height="30" width="30" bgcolor="#cdba96"></td>
                            <td>#CDBA96</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cdb7b5"></td>
                            <td>#CDB7B5</td>
                            <td height="30" width="30" bgcolor="#cdb79e"></td>
                            <td>#CDB79E</td>
                            <td height="30" width="30" bgcolor="#cdb5cd"></td>
                            <td>#CDB5CD</td>
                            <td height="30" width="30" bgcolor="#cdb38b"></td>
                            <td>#CDB38B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cdaf95"></td>
                            <td>#CDAF95</td>
                            <td height="30" width="30" bgcolor="#cdad00"></td>
                            <td>#CDAD00</td>
                            <td height="30" width="30" bgcolor="#cdaa7d"></td>
                            <td>#CDAA7D</td>
                            <td height="30" width="30" bgcolor="#cd9b9b"></td>
                            <td>#CD9B9B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cd9b1d"></td>
                            <td>#CD9B1D</td>
                            <td height="30" width="30" bgcolor="#cd96cd"></td>
                            <td>#CD96CD</td>
                            <td height="30" width="30" bgcolor="#cd950c"></td>
                            <td>#CD950C</td>
                            <td height="30" width="30" bgcolor="#cd919e"></td>
                            <td>#CD919E</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cd8c95"></td>
                            <td>#CD8C95</td>
                            <td height="30" width="30" bgcolor="#cd853f"></td>
                            <td>#CD853F</td>
                            <td height="30" width="30" bgcolor="#cd8500"></td>
                            <td>#CD8500</td>
                            <td height="30" width="30" bgcolor="#cd8162"></td>
                            <td>#CD8162</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cd7054"></td>
                            <td>#CD7054</td>
                            <td height="30" width="30" bgcolor="#cd69c9"></td>
                            <td>#CD69C9</td>
                            <td height="30" width="30" bgcolor="#cd6889"></td>
                            <td>#CD6889</td>
                            <td height="30" width="30" bgcolor="#cd6839"></td>
                            <td>#CD6839</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cd661d"></td>
                            <td>#CD661D</td>
                            <td height="30" width="30" bgcolor="#cd6600"></td>
                            <td>#CD6600</td>
                            <td height="30" width="30" bgcolor="#cd6090"></td>
                            <td>#CD6090</td>
                            <td height="30" width="30" bgcolor="#cd5c5c"></td>
                            <td>#CD5C5C</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cd5b45"></td>
                            <td>#CD5B45</td>
                            <td height="30" width="30" bgcolor="#cd5555"></td>
                            <td>#CD5555</td>
                            <td height="30" width="30" bgcolor="#cd4f39"></td>
                            <td>#CD4F39</td>
                            <td height="30" width="30" bgcolor="#cd3700"></td>
                            <td>#CD3700</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cd3333"></td>
                            <td>#CD3333</td>
                            <td height="30" width="30" bgcolor="#cd3278"></td>
                            <td>#CD3278</td>
                            <td height="30" width="30" bgcolor="#cd2990"></td>
                            <td>#CD2990</td>
                            <td height="30" width="30" bgcolor="#cd2626"></td>
                            <td>#CD2626</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#cd1076"></td>
                            <td>#CD1076</td>
                            <td height="30" width="30" bgcolor="#cd00cd"></td>
                            <td>#CD00CD</td>
                            <td height="30" width="30" bgcolor="#cd0000"></td>
                            <td>#CD0000</td>
                            <td height="30" width="30" bgcolor="#cccccc"></td>
                            <td>#CCCCCC</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#caff70"></td>
                            <td>#CAFF70</td>
                            <td height="30" width="30" bgcolor="#cae1ff"></td>
                            <td>#CAE1FF</td>
                            <td height="30" width="30" bgcolor="#c9c9c9"></td>
                            <td>#C9C9C9</td>
                            <td height="30" width="30" bgcolor="#c7c7c7"></td>
                            <td>#C7C7C7</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#c71585"></td>
                            <td>#C71585</td>
                            <td height="30" width="30" bgcolor="#c6e2ff"></td>
                            <td>#C6E2FF</td>
                            <td height="30" width="30" bgcolor="#c67171"></td>
                            <td>#C67171</td>
                            <td height="30" width="30" bgcolor="#c5c1aa"></td>
                            <td>#C5C1AA</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#c4c4c4"></td>
                            <td>#C4C4C4</td>
                            <td height="30" width="30" bgcolor="#c2c2c2"></td>
                            <td>#C2C2C2</td>
                            <td height="30" width="30" bgcolor="#c1ffc1"></td>
                            <td>#C1FFC1</td>
                            <td height="30" width="30" bgcolor="#c1cdcd"></td>
                            <td>#C1CDCD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#c1cdc1"></td>
                            <td>#C1CDC1</td>
                            <td height="30" width="30" bgcolor="#c1c1c1"></td>
                            <td>#C1C1C1</td>
                            <td height="30" width="30" bgcolor="#c0ff3e"></td>
                            <td>#C0FF3E</td>
                            <td height="30" width="30" bgcolor="#bfefff"></td>
                            <td>#BFEFFF</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#bfbfbf"></td>
                            <td>#BFBFBF</td>
                            <td height="30" width="30" bgcolor="#bf3eff"></td>
                            <td>#BF3EFF</td>
                            <td height="30" width="30" bgcolor="#bebebe"></td>
                            <td>#BEBEBE</td>
                            <td height="30" width="30" bgcolor="#bdbdbd"></td>
                            <td>#BDBDBD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#bdb76b"></td>
                            <td>#BDB76B</td>
                            <td height="30" width="30" bgcolor="#bcee68"></td>
                            <td>#BCEE68</td>
                            <td height="30" width="30" bgcolor="#bcd2ee"></td>
                            <td>#BCD2EE</td>
                            <td height="30" width="30" bgcolor="#bc8f8f"></td>
                            <td>#BC8F8F</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#bbffff"></td>
                            <td>#BBFFFF</td>
                            <td height="30" width="30" bgcolor="#bababa"></td>
                            <td>#BABABA</td>
                            <td height="30" width="30" bgcolor="#ba55d3"></td>
                            <td>#BA55D3</td>
                            <td height="30" width="30" bgcolor="#b9d3ee"></td>
                            <td>#B9D3EE</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#b8b8b8"></td>
                            <td>#B8B8B8</td>
                            <td height="30" width="30" bgcolor="#b8860b"></td>
                            <td>#B8860B</td>
                            <td height="30" width="30" bgcolor="#b7b7b7"></td>
                            <td>#B7B7B7</td>
                            <td height="30" width="30" bgcolor="#b5b5b5"></td>
                            <td>#B5B5B5</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#b4eeb4"></td>
                            <td>#B4EEB4</td>
                            <td height="30" width="30" bgcolor="#b4cdcd"></td>
                            <td>#B4CDCD</td>
                            <td height="30" width="30" bgcolor="#b452cd"></td>
                            <td>#B452CD</td>
                            <td height="30" width="30" bgcolor="#b3ee3a"></td>
                            <td>#B3EE3A</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#b3b3b3"></td>
                            <td>#B3B3B3</td>
                            <td height="30" width="30" bgcolor="#b2dfee"></td>
                            <td>#B2DFEE</td>
                            <td height="30" width="30" bgcolor="#b23aee"></td>
                            <td>#B23AEE</td>
                            <td height="30" width="30" bgcolor="#b22222"></td>
                            <td>#B22222</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#b0e2ff"></td>
                            <td>#B0E2FF</td>
                            <td height="30" width="30" bgcolor="#b0e0e6"></td>
                            <td>#B0E0E6</td>
                            <td height="30" width="30" bgcolor="#b0c4de"></td>
                            <td>#B0C4DE</td>
                            <td height="30" width="30" bgcolor="#b0b0b0"></td>
                            <td>#B0B0B0</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#b03060"></td>
                            <td>#B03060</td>
                            <td height="30" width="30" bgcolor="#aeeeee"></td>
                            <td>#AEEEEE</td>
                            <td height="30" width="30" bgcolor="#adff2f"></td>
                            <td>#ADFF2F</td>
                            <td height="30" width="30" bgcolor="#add8e6"></td>
                            <td>#ADD8E6</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#adadad"></td>
                            <td>#ADADAD</td>
                            <td height="30" width="30" bgcolor="#ababab"></td>
                            <td>#ABABAB</td>
                            <td height="30" width="30" bgcolor="#ab82ff"></td>
                            <td>#AB82FF</td>
                            <td height="30" width="30" bgcolor="#aaaaaa"></td>
                            <td>#AAAAAA</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#a9a9a9"></td>
                            <td>#A9A9A9</td>
                            <td height="30" width="30" bgcolor="#a8a8a8"></td>
                            <td>#A8A8A8</td>
                            <td height="30" width="30" bgcolor="#a6a6a6"></td>
                            <td>#A6A6A6</td>
                            <td height="30" width="30" bgcolor="#a52a2a"></td>
                            <td>#A52A2A</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#a4d3ee"></td>
                            <td>#A4D3EE</td>
                            <td height="30" width="30" bgcolor="#a3a3a3"></td>
                            <td>#A3A3A3</td>
                            <td height="30" width="30" bgcolor="#a2cd5a"></td>
                            <td>#A2CD5A</td>
                            <td height="30" width="30" bgcolor="#a2b5cd"></td>
                            <td>#A2B5CD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#a1a1a1"></td>
                            <td>#A1A1A1</td>
                            <td height="30" width="30" bgcolor="#a0522d"></td>
                            <td>#A0522D</td>
                            <td height="30" width="30" bgcolor="#a020f0"></td>
                            <td>#A020F0</td>
                            <td height="30" width="30" bgcolor="#9fb6cd"></td>
                            <td>#9FB6CD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#9f79ee"></td>
                            <td>#9F79EE</td>
                            <td height="30" width="30" bgcolor="#9e9e9e"></td>
                            <td>#9E9E9E</td>
                            <td height="30" width="30" bgcolor="#9c9c9c"></td>
                            <td>#9C9C9C</td>
                            <td height="30" width="30" bgcolor="#9bcd9b"></td>
                            <td>#9BCD9B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#9b30ff"></td>
                            <td>#9B30FF</td>
                            <td height="30" width="30" bgcolor="#9aff9a"></td>
                            <td>#9AFF9A</td>
                            <td height="30" width="30" bgcolor="#9acd32"></td>
                            <td>#9ACD32</td>
                            <td height="30" width="30" bgcolor="#9ac0cd"></td>
                            <td>#9AC0CD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#9a32cd"></td>
                            <td>#9A32CD</td>
                            <td height="30" width="30" bgcolor="#999999"></td>
                            <td>#999999</td>
                            <td height="30" width="30" bgcolor="#9932cc"></td>
                            <td>#9932CC</td>
                            <td height="30" width="30" bgcolor="#98fb98"></td>
                            <td>#98FB98</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#98f5ff"></td>
                            <td>#98F5FF</td>
                            <td height="30" width="30" bgcolor="#97ffff"></td>
                            <td>#97FFFF</td>
                            <td height="30" width="30" bgcolor="#96cdcd"></td>
                            <td>#96CDCD</td>
                            <td height="30" width="30" bgcolor="#969696"></td>
                            <td>#969696</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#949494"></td>
                            <td>#949494</td>
                            <td height="30" width="30" bgcolor="#9400d3"></td>
                            <td>#9400D3</td>
                            <td height="30" width="30" bgcolor="#9370db"></td>
                            <td>#9370DB</td>
                            <td height="30" width="30" bgcolor="#919191"></td>
                            <td>#919191</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#912cee"></td>
                            <td>#912CEE</td>
                            <td height="30" width="30" bgcolor="#90ee90"></td>
                            <td>#90EE90</td>
                            <td height="30" width="30" bgcolor="#8fbc8f"></td>
                            <td>#8FBC8F</td>
                            <td height="30" width="30" bgcolor="#8f8f8f"></td>
                            <td>#8F8F8F</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8ee5ee"></td>
                            <td>#8EE5EE</td>
                            <td height="30" width="30" bgcolor="#8e8e8e"></td>
                            <td>#8E8E8E</td>
                            <td height="30" width="30" bgcolor="#8e8e38"></td>
                            <td>#8E8E38</td>
                            <td height="30" width="30" bgcolor="#8e388e"></td>
                            <td>#8E388E</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8deeee"></td>
                            <td>#8DEEEE</td>
                            <td height="30" width="30" bgcolor="#8db6cd"></td>
                            <td>#8DB6CD</td>
                            <td height="30" width="30" bgcolor="#8c8c8c"></td>
                            <td>#8C8C8C</td>
                            <td height="30" width="30" bgcolor="#8b8b83"></td>
                            <td>#8B8B83</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b8b7a"></td>
                            <td>#8B8B7A</td>
                            <td height="30" width="30" bgcolor="#8b8b00"></td>
                            <td>#8B8B00</td>
                            <td height="30" width="30" bgcolor="#8b8989"></td>
                            <td>#8B8989</td>
                            <td height="30" width="30" bgcolor="#8b8970"></td>
                            <td>#8B8970</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b8878"></td>
                            <td>#8B8878</td>
                            <td height="30" width="30" bgcolor="#8b8682"></td>
                            <td>#8B8682</td>
                            <td height="30" width="30" bgcolor="#8b864e"></td>
                            <td>#8B864E</td>
                            <td height="30" width="30" bgcolor="#8b8386"></td>
                            <td>#8B8386</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b8378"></td>
                            <td>#8B8378</td>
                            <td height="30" width="30" bgcolor="#8b814c"></td>
                            <td>#8B814C</td>
                            <td height="30" width="30" bgcolor="#8b7e66"></td>
                            <td>#8B7E66</td>
                            <td height="30" width="30" bgcolor="#8b7d7b"></td>
                            <td>#8B7D7B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b7d6b"></td>
                            <td>#8B7D6B</td>
                            <td height="30" width="30" bgcolor="#8b7b8b"></td>
                            <td>#8B7B8B</td>
                            <td height="30" width="30" bgcolor="#8b795e"></td>
                            <td>#8B795E</td>
                            <td height="30" width="30" bgcolor="#8b7765"></td>
                            <td>#8B7765</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b7500"></td>
                            <td>#8B7500</td>
                            <td height="30" width="30" bgcolor="#8b7355"></td>
                            <td>#8B7355</td>
                            <td height="30" width="30" bgcolor="#8b6969"></td>
                            <td>#8B6969</td>
                            <td height="30" width="30" bgcolor="#8b6914"></td>
                            <td>#8B6914</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b668b"></td>
                            <td>#8B668B</td>
                            <td height="30" width="30" bgcolor="#8b6508"></td>
                            <td>#8B6508</td>
                            <td height="30" width="30" bgcolor="#8b636c"></td>
                            <td>#8B636C</td>
                            <td height="30" width="30" bgcolor="#8b5f65"></td>
                            <td>#8B5F65</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b5a2b"></td>
                            <td>#8B5A2B</td>
                            <td height="30" width="30" bgcolor="#8b5a00"></td>
                            <td>#8B5A00</td>
                            <td height="30" width="30" bgcolor="#8b5742"></td>
                            <td>#8B5742</td>
                            <td height="30" width="30" bgcolor="#8b4c39"></td>
                            <td>#8B4C39</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b4789"></td>
                            <td>#8B4789</td>
                            <td height="30" width="30" bgcolor="#8b475d"></td>
                            <td>#8B475D</td>
                            <td height="30" width="30" bgcolor="#8b4726"></td>
                            <td>#8B4726</td>
                            <td height="30" width="30" bgcolor="#8b4513"></td>
                            <td>#8B4513</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b4500"></td>
                            <td>#8B4500</td>
                            <td height="30" width="30" bgcolor="#8b3e2f"></td>
                            <td>#8B3E2F</td>
                            <td height="30" width="30" bgcolor="#8b3a62"></td>
                            <td>#8B3A62</td>
                            <td height="30" width="30" bgcolor="#8b3a3a"></td>
                            <td>#8B3A3A</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b3626"></td>
                            <td>#8B3626</td>
                            <td height="30" width="30" bgcolor="#8b2500"></td>
                            <td>#8B2500</td>
                            <td height="30" width="30" bgcolor="#8b2323"></td>
                            <td>#8B2323</td>
                            <td height="30" width="30" bgcolor="#8b2252"></td>
                            <td>#8B2252</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b1c62"></td>
                            <td>#8B1C62</td>
                            <td height="30" width="30" bgcolor="#8b1a1a"></td>
                            <td>#8B1A1A</td>
                            <td height="30" width="30" bgcolor="#8b0a50"></td>
                            <td>#8B0A50</td>
                            <td height="30" width="30" bgcolor="#8b008b"></td>
                            <td>#8B008B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#8b0000"></td>
                            <td>#8B0000</td>
                            <td height="30" width="30" bgcolor="#8a8a8a"></td>
                            <td>#8A8A8A</td>
                            <td height="30" width="30" bgcolor="#8a2be2"></td>
                            <td>#8A2BE2</td>
                            <td height="30" width="30" bgcolor="#8968cd"></td>
                            <td>#8968CD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#87ceff"></td>
                            <td>#87CEFF</td>
                            <td height="30" width="30" bgcolor="#87cefa"></td>
                            <td>#87CEFA</td>
                            <td height="30" width="30" bgcolor="#87ceeb"></td>
                            <td>#87CEEB</td>
                            <td height="30" width="30" bgcolor="#878787"></td>
                            <td>#878787</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#858585"></td>
                            <td>#858585</td>
                            <td height="30" width="30" bgcolor="#848484"></td>
                            <td>#848484</td>
                            <td height="30" width="30" bgcolor="#8470ff"></td>
                            <td>#8470FF</td>
                            <td height="30" width="30" bgcolor="#838b8b"></td>
                            <td>#838B8B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#838b83"></td>
                            <td>#838B83</td>
                            <td height="30" width="30" bgcolor="#836fff"></td>
                            <td>#836FFF</td>
                            <td height="30" width="30" bgcolor="#828282"></td>
                            <td>#828282</td>
                            <td height="30" width="30" bgcolor="#7fffd4"></td>
                            <td>#7FFFD4</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#7fff00"></td>
                            <td>#7FFF00</td>
                            <td height="30" width="30" bgcolor="#7f7f7f"></td>
                            <td>#7F7F7F</td>
                            <td height="30" width="30" bgcolor="#7ec0ee"></td>
                            <td>#7EC0EE</td>
                            <td height="30" width="30" bgcolor="#7d9ec0"></td>
                            <td>#7D9EC0</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#7d7d7d"></td>
                            <td>#7D7D7D</td>
                            <td height="30" width="30" bgcolor="#7d26cd"></td>
                            <td>#7D26CD</td>
                            <td height="30" width="30" bgcolor="#7cfc00"></td>
                            <td>#7CFC00</td>
                            <td height="30" width="30" bgcolor="#7ccd7c"></td>
                            <td>#7CCD7C</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#7b68ee"></td>
                            <td>#7B68EE</td>
                            <td height="30" width="30" bgcolor="#7ac5cd"></td>
                            <td>#7AC5CD</td>
                            <td height="30" width="30" bgcolor="#7a8b8b"></td>
                            <td>#7A8B8B</td>
                            <td height="30" width="30" bgcolor="#7a7a7a"></td>
                            <td>#7A7A7A</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#7a67ee"></td>
                            <td>#7A67EE</td>
                            <td height="30" width="30" bgcolor="#7a378b"></td>
                            <td>#7A378B</td>
                            <td height="30" width="30" bgcolor="#79cdcd"></td>
                            <td>#79CDCD</td>
                            <td height="30" width="30" bgcolor="#787878"></td>
                            <td>#787878</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#778899"></td>
                            <td>#778899</td>
                            <td height="30" width="30" bgcolor="#76eec6"></td>
                            <td>#76EEC6</td>
                            <td height="30" width="30" bgcolor="#76ee00"></td>
                            <td>#76EE00</td>
                            <td height="30" width="30" bgcolor="#757575"></td>
                            <td>#757575</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#737373"></td>
                            <td>#737373</td>
                            <td height="30" width="30" bgcolor="#71c671"></td>
                            <td>#71C671</td>
                            <td height="30" width="30" bgcolor="#7171c6"></td>
                            <td>#7171C6</td>
                            <td height="30" width="30" bgcolor="#708090"></td>
                            <td>#708090</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#707070"></td>
                            <td>#707070</td>
                            <td height="30" width="30" bgcolor="#6e8b3d"></td>
                            <td>#6E8B3D</td>
                            <td height="30" width="30" bgcolor="#6e7b8b"></td>
                            <td>#6E7B8B</td>
                            <td height="30" width="30" bgcolor="#6e6e6e"></td>
                            <td>#6E6E6E</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#6ca6cd"></td>
                            <td>#6CA6CD</td>
                            <td height="30" width="30" bgcolor="#6c7b8b"></td>
                            <td>#6C7B8B</td>
                            <td height="30" width="30" bgcolor="#6b8e23"></td>
                            <td>#6B8E23</td>
                            <td height="30" width="30" bgcolor="#6b6b6b"></td>
                            <td>#6B6B6B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#6a5acd"></td>
                            <td>#6A5ACD</td>
                            <td height="30" width="30" bgcolor="#698b69"></td>
                            <td>#698B69</td>
                            <td height="30" width="30" bgcolor="#698b22"></td>
                            <td>#698B22</td>
                            <td height="30" width="30" bgcolor="#696969"></td>
                            <td>#696969</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#6959cd"></td>
                            <td>#6959CD</td>
                            <td height="30" width="30" bgcolor="#68838b"></td>
                            <td>#68838B</td>
                            <td height="30" width="30" bgcolor="#68228b"></td>
                            <td>#68228B</td>
                            <td height="30" width="30" bgcolor="#66cdaa"></td>
                            <td>#66CDAA</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#66cd00"></td>
                            <td>#66CD00</td>
                            <td height="30" width="30" bgcolor="#668b8b"></td>
                            <td>#668B8B</td>
                            <td height="30" width="30" bgcolor="#666666"></td>
                            <td>#666666</td>
                            <td height="30" width="30" bgcolor="#6495ed"></td>
                            <td>#6495ED</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#63b8ff"></td>
                            <td>#63B8FF</td>
                            <td height="30" width="30" bgcolor="#636363"></td>
                            <td>#636363</td>
                            <td height="30" width="30" bgcolor="#616161"></td>
                            <td>#616161</td>
                            <td height="30" width="30" bgcolor="#607b8b"></td>
                            <td>#607B8B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#5f9ea0"></td>
                            <td>#5F9EA0</td>
                            <td height="30" width="30" bgcolor="#5e5e5e"></td>
                            <td>#5E5E5E</td>
                            <td height="30" width="30" bgcolor="#5d478b"></td>
                            <td>#5D478B</td>
                            <td height="30" width="30" bgcolor="#5cacee"></td>
                            <td>#5CACEE</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#5c5c5c"></td>
                            <td>#5C5C5C</td>
                            <td height="30" width="30" bgcolor="#5b5b5b"></td>
                            <td>#5B5B5B</td>
                            <td height="30" width="30" bgcolor="#595959"></td>
                            <td>#595959</td>
                            <td height="30" width="30" bgcolor="#575757"></td>
                            <td>#575757</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#556b2f"></td>
                            <td>#556B2F</td>
                            <td height="30" width="30" bgcolor="#555555"></td>
                            <td>#555555</td>
                            <td height="30" width="30" bgcolor="#551a8b"></td>
                            <td>#551A8B</td>
                            <td height="30" width="30" bgcolor="#54ff9f"></td>
                            <td>#54FF9F</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#548b54"></td>
                            <td>#548B54</td>
                            <td height="30" width="30" bgcolor="#545454"></td>
                            <td>#545454</td>
                            <td height="30" width="30" bgcolor="#53868b"></td>
                            <td>#53868B</td>
                            <td height="30" width="30" bgcolor="#528b8b"></td>
                            <td>#528B8B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#525252"></td>
                            <td>#525252</td>
                            <td height="30" width="30" bgcolor="#515151"></td>
                            <td>#515151</td>
                            <td height="30" width="30" bgcolor="#4f94cd"></td>
                            <td>#4F94CD</td>
                            <td height="30" width="30" bgcolor="#4f4f4f"></td>
                            <td>#4F4F4F</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#4eee94"></td>
                            <td>#4EEE94</td>
                            <td height="30" width="30" bgcolor="#4d4d4d"></td>
                            <td>#4D4D4D</td>
                            <td height="30" width="30" bgcolor="#4b0082"></td>
                            <td>#4B0082</td>
                            <td height="30" width="30" bgcolor="#4a708b"></td>
                            <td>#4A708B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#4a4a4a"></td>
                            <td>#4A4A4A</td>
                            <td height="30" width="30" bgcolor="#48d1cc"></td>
                            <td>#48D1CC</td>
                            <td height="30" width="30" bgcolor="#4876ff"></td>
                            <td>#4876FF</td>
                            <td height="30" width="30" bgcolor="#483d8b"></td>
                            <td>#483D8B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#474747"></td>
                            <td>#474747</td>
                            <td height="30" width="30" bgcolor="#473c8b"></td>
                            <td>#473C8B</td>
                            <td height="30" width="30" bgcolor="#4682b4"></td>
                            <td>#4682B4</td>
                            <td height="30" width="30" bgcolor="#458b74"></td>
                            <td>#458B74</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#458b00"></td>
                            <td>#458B00</td>
                            <td height="30" width="30" bgcolor="#454545"></td>
                            <td>#454545</td>
                            <td height="30" width="30" bgcolor="#43cd80"></td>
                            <td>#43CD80</td>
                            <td height="30" width="30" bgcolor="#436eee"></td>
                            <td>#436EEE</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#424242"></td>
                            <td>#424242</td>
                            <td height="30" width="30" bgcolor="#4169e1"></td>
                            <td>#4169E1</td>
                            <td height="30" width="30" bgcolor="#40e0d0"></td>
                            <td>#40E0D0</td>
                            <td height="30" width="30" bgcolor="#404040"></td>
                            <td>#404040</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#3d3d3d"></td>
                            <td>#3D3D3D</td>
                            <td height="30" width="30" bgcolor="#3cb371"></td>
                            <td>#3CB371</td>
                            <td height="30" width="30" bgcolor="#3b3b3b"></td>
                            <td>#3B3B3B</td>
                            <td height="30" width="30" bgcolor="#3a5fcd"></td>
                            <td>#3A5FCD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#388e8e"></td>
                            <td>#388E8E</td>
                            <td height="30" width="30" bgcolor="#383838"></td>
                            <td>#383838</td>
                            <td height="30" width="30" bgcolor="#36648b"></td>
                            <td>#36648B</td>
                            <td height="30" width="30" bgcolor="#363636"></td>
                            <td>#363636</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#333333"></td>
                            <td>#333333</td>
                            <td height="30" width="30" bgcolor="#32cd32"></td>
                            <td>#32CD32</td>
                            <td height="30" width="30" bgcolor="#303030"></td>
                            <td>#303030</td>
                            <td height="30" width="30" bgcolor="#2f4f4f"></td>
                            <td>#2F4F4F</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#2e8b57"></td>
                            <td>#2E8B57</td>
                            <td height="30" width="30" bgcolor="#2e2e2e"></td>
                            <td>#2E2E2E</td>
                            <td height="30" width="30" bgcolor="#2b2b2b"></td>
                            <td>#2B2B2B</td>
                            <td height="30" width="30" bgcolor="#292929"></td>
                            <td>#292929</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#282828"></td>
                            <td>#282828</td>
                            <td height="30" width="30" bgcolor="#27408b"></td>
                            <td>#27408B</td>
                            <td height="30" width="30" bgcolor="#262626"></td>
                            <td>#262626</td>
                            <td height="30" width="30" bgcolor="#242424"></td>
                            <td>#242424</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#228b22"></td>
                            <td>#228B22</td>
                            <td height="30" width="30" bgcolor="#218868"></td>
                            <td>#218868</td>
                            <td height="30" width="30" bgcolor="#212121"></td>
                            <td>#212121</td>
                            <td height="30" width="30" bgcolor="#20b2aa"></td>
                            <td>#20B2AA</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#1f1f1f"></td>
                            <td>#1F1F1F</td>
                            <td height="30" width="30" bgcolor="#1e90ff"></td>
                            <td>#1E90FF</td>
                            <td height="30" width="30" bgcolor="#1e1e1e"></td>
                            <td>#1E1E1E</td>
                            <td height="30" width="30" bgcolor="#1c86ee"></td>
                            <td>#1C86EE</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#1c1c1c"></td>
                            <td>#1C1C1C</td>
                            <td height="30" width="30" bgcolor="#1a1a1a"></td>
                            <td>#1A1A1A</td>
                            <td height="30" width="30" bgcolor="#191970"></td>
                            <td>#191970</td>
                            <td height="30" width="30" bgcolor="#1874cd"></td>
                            <td>#1874CD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#171717"></td>
                            <td>#171717</td>
                            <td height="30" width="30" bgcolor="#141414"></td>
                            <td>#141414</td>
                            <td height="30" width="30" bgcolor="#121212"></td>
                            <td>#121212</td>
                            <td height="30" width="30" bgcolor="#104e8b"></td>
                            <td>#104E8B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#0f0f0f"></td>
                            <td>#0F0F0F</td>
                            <td height="30" width="30" bgcolor="#0d0d0d"></td>
                            <td>#0D0D0D</td>
                            <td height="30" width="30" bgcolor="#0a0a0a"></td>
                            <td>#0A0A0A</td>
                            <td height="30" width="30" bgcolor="#080808"></td>
                            <td>#080808</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#050505"></td>
                            <td>#050505</td>
                            <td height="30" width="30" bgcolor="#030303"></td>
                            <td>#030303</td>
                            <td height="30" width="30" bgcolor="#00ffff"></td>
                            <td>#00FFFF</td>
                            <td height="30" width="30" bgcolor="#00ff7f"></td>
                            <td>#00FF7F</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#00ff00"></td>
                            <td>#00FF00</td>
                            <td height="30" width="30" bgcolor="#00fa9a"></td>
                            <td>#00FA9A</td>
                            <td height="30" width="30" bgcolor="#00f5ff"></td>
                            <td>#00F5FF</td>
                            <td height="30" width="30" bgcolor="#00eeee"></td>
                            <td>#00EEEE</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#00ee76"></td>
                            <td>#00EE76</td>
                            <td height="30" width="30" bgcolor="#00ee00"></td>
                            <td>#00EE00</td>
                            <td height="30" width="30" bgcolor="#00e5ee"></td>
                            <td>#00E5EE</td>
                            <td height="30" width="30" bgcolor="#00ced1"></td>
                            <td>#00CED1</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#00cdcd"></td>
                            <td>#00CDCD</td>
                            <td height="30" width="30" bgcolor="#00cd66"></td>
                            <td>#00CD66</td>
                            <td height="30" width="30" bgcolor="#00cd00"></td>
                            <td>#00CD00</td>
                            <td height="30" width="30" bgcolor="#00c5cd"></td>
                            <td>#00C5CD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#00bfff"></td>
                            <td>#00BFFF</td>
                            <td height="30" width="30" bgcolor="#00b2ee"></td>
                            <td>#00B2EE</td>
                            <td height="30" width="30" bgcolor="#009acd"></td>
                            <td>#009ACD</td>
                            <td height="30" width="30" bgcolor="#008b8b"></td>
                            <td>#008B8B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#008b45"></td>
                            <td>#008B45</td>
                            <td height="30" width="30" bgcolor="#008b00"></td>
                            <td>#008B00</td>
                            <td height="30" width="30" bgcolor="#00868b"></td>
                            <td>#00868B</td>
                            <td height="30" width="30" bgcolor="#00688b"></td>
                            <td>#00688B</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#006400"></td>
                            <td>#006400</td>
                            <td height="30" width="30" bgcolor="#0000ff"></td>
                            <td>#0000FF</td>
                            <td height="30" width="30" bgcolor="#0000ee"></td>
                            <td>#0000EE</td>
                            <td height="30" width="30" bgcolor="#0000cd"></td>
                            <td>#0000CD</td>
                          </tr>
                          <tr>
                            <td height="30" width="30" bgcolor="#0000aa"></td>
                            <td>#0000AA</td>
                            <td height="30" width="30" bgcolor="#00008b"></td>
                            <td>#00008B</td>
                            <td height="30" width="30" bgcolor="#000080"></td>
                            <td>#000080</td>
                            <td height="30" width="30" bgcolor="#000000"></td>
                            <td>#000000</td>
                          </tr>"""
soup = BeautifulSoup(colors,'lxml')
print(soup.get("td"))
