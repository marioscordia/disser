const items = [
  "doi.org/10.1016/j.array.2025.100625",
  "doi.org/10.58346/JISIS.2026.I1.008",
  "doi.org/10.3390/electronics15010101",
  "doi.org/10.3390/app15115830",
  "doi.org/10.1111/coin.70034",
  "doi.org/10.1109/OJCS.2024.3517154",
  "doi.org/10.32604/cmes.2024.056816",
  "doi.org/10.1016/j.procs.2025.04.558",
  "doi.org/10.18280/ijsse.150112",
  "doi.org/10.1155/int/9722173",
  "doi.org/10.3390/engproc2025107059",
  "doi.org/10.1016/j.neucom.2024.128673",
  "doi.org/10.52549/ijeei.v12i4.5787",
  "doi.org/10.11591/ijai.v13.i3.pp2666-2673",
  "doi.org/10.1002/aisy.202300706",
  "doi.org/10.37936/ecti-cit.2024183.255679",
  "doi.org/10.5753/jbcs.2024.3282",
  "doi.org/10.1016/j.iswa.2023.200311",
  "doi.org/10.1007/s11042-023-16231-x",
  "doi.org/10.1016/j.procs.2024.09.465",
  "doi.org/10.7717/PEERJ-CS.1939",
  "doi.org/10.1109/ACCESS.2024.3380192",
  "doi.org/10.3390/s24020317",
  "doi.org/10.3390/computers12090175",
  "doi.org/10.1016/j.cviu.2023.103739",
  "doi.org/10.33103/uot.ijccce.23.2.16",
  "doi.org/10.3390/info14040240",
  "doi.org/10.1007/s10489-022-03613-1",
  "doi.org/10.3390/sym15020528",
  "doi.org/10.14569/IJACSA.2023.0140578",
  "doi.org/10.22266/ijies2023.0831.36",
  "doi.org/10.14569/IJACSA.2023.0140891",
  "doi.org/10.1109/ACCESS.2023.3310885",
  "doi.org/10.9781/ijimai.2023.05.006",
  "doi.org/10.32604/csse.2023.034805",
  "doi.org/10.1038/s41598-022-07137-z",
  "doi.org/10.3390/s22239383",
  "doi.org/10.3390/app12125772",
  "doi.org/10.3390/math10091555",
  "doi.org/10.3390/s22062216",
  "doi.org/10.1155/2022/5362093",
  "doi.org/10.32604/iasc.2022.021061",
  "doi.org/10.32985/ijeces.13.8.7",
  "doi.org/10.1016/j.procs.2023.01.202",
  "doi.org/10.1016/j.rineng.2023.101026",
  "doi.org/10.1038/s41598-025-12531-4",
  "doi.org/10.1016/j.aej.2025.06.035",
  "doi.org/10.3389/fcomp.2023.1274928",
  "doi.org/10.33039/ami.2025.10.015",
  "doi.org/10.32604/cmc.2022.024566"
];

const email = "axmetovmed@gmail.com";
const fs = require('fs');
const https = require('https');

function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => {
        data += chunk;
      });
      res.on('end', () => {
        try {
          resolve(JSON.parse(data));
        } catch (e) {
          reject(e);
        }
      });
    }).on('error', (err) => {
      reject(err);
    });
  });
}

function getApaCitation(data) {
  if (data && data.citations) {
    const apa = data.citations.find(function (c) {
      return c.style_shortname === 'apa';
    });
    if (apa) {
      return apa.citation;
    }
  }
  return null;
}

async function processItems() {
  console.log('Starting to fetch metadata for ' + items.length + ' items...');
  const fd = fs.openSync('references.txt', 'w');

  for (const item of items) {
    // Basic encoding
    const encodedItem = encodeURIComponent(item);
    const url = 'https://api.citeas.org/product/' + encodedItem + '?email=' + email;

    try {
      console.log('Fetching: ' + item);
      const data = await fetchUrl(url);

      const citation = getApaCitation(data);

      if (citation) {
        console.log('[SUCCESS] ' + item);
        console.log(citation + '\n');
        fs.writeSync(fd, citation + '\n\n');
      } else {
        console.log('[WARN] No APA citation found for ' + item);
        fs.writeSync(fd, '[MISSING] ' + item + '\n\n');
      }

      // Be nice to the API
      await new Promise(resolve => setTimeout(resolve, 500));

    } catch (error) {
      console.error('[ERROR] Failed to fetch ' + item + ': ' + error.message);
      fs.writeSync(fd, '[ERROR] ' + item + '\n\n');
    }
  }
  fs.closeSync(fd);
  console.log("Finished processing all items. Results written to references.txt");
}

processItems();
