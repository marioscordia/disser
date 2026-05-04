const items = [
  "doi.org/10.1145/3576924",
  "doi.org/10.1145/3477495.3532082",
  "doi.org/10.1145/3746252.3761377",
  "doi.org/10.1145/3637528.3671458",
  "doi.org/10.1145/3631939",
  "doi.org/10.1145/3746252.3761077",
  "doi.org/10.1145/3485447.3511955",
  "doi.org/10.1145/3746252.3761211",
  "doi.org/10.1145/3701716.3717859",
  "doi.org/10.1145/3746252.3761238",
  "doi.org/10.1145/3722552",
  "doi.org/10.1145/3580305.3599892",
  "doi.org/10.1145/3746252.3761059",
  "doi.org/10.1145/3746027.3762039",
  "doi.org/10.1145/3726302.3729971",
  "doi.org/10.1145/3634911",
  "doi.org/10.1145/3603167",
  "doi.org/10.1145/3746252.3761484",
  "doi.org/10.1145/3539618.3594247",
  "doi.org/10.1145/3511808.3557483",
  "doi.org/10.1145/3488560.3498495",
  "doi.org/10.1145/3726302.3730046",
  "doi.org/10.48084/etasr.9450",
  "doi.org/10.3389/fdata.2021.622106",
  "doi.org/10.3389/frai.2025.1697169",
  "https://www.researchgate.net/publication/398402921_Boosting_Webpage_Retrieval_with_Ensemble_Learning_and_Advanced_Semantic_Models_A_Novel_Re-Ranking_Framework",
  "doi.org/10.1109/ACCESS.2025.3571184",
  "doi.org/10.1109/ACCESS.2025.3625652",
  "doi.org/10.1109/ACCESS.2025.3550964",
  "doi.org/10.1109/JIOT.2024.3522219",
  "doi.org/10.1109/ACCESS.2025.3526885",
  "doi.org/10.1109/ACCESS.2024.3428630",
  "doi.org/10.1109/ACCESS.2025.3576253",
  "doi.org/10.3390/electronics14224448",
  "doi.org/10.3390/info16020151",
  "doi.org/10.1016/j.knosys.2022.108545",
  "doi.org/10.1016/j.procs.2025.09.302",
  "doi.org/10.1016/j.asej.2025.103853",
  "doi.org/10.1007/s10844-025-01009-4",
  "doi.org/10.1007/s10462-024-10939-4",
  "doi.org/10.1007/978-981-96-7508-1_12",
  "doi.org/10.1007/s10791-022-09405-y",
  "doi.org/10.1007/978-3-031-56066-8_29",
  "doi.org/10.1007/s00500-022-07433-w",
  "doi.org/10.1007/978-3-030-72113-8_16",
  "doi.org/10.1007/978-3-031-73147-1_6",
  "doi.org/10.7759/s44404-025-08244-6",
  "doi.org/10.30574/wjaets.2025.15.1.0216",
  "doi.org/10.1142/S0218488522500246"
];

const email = "gybraty@gmail.com";
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
     const apa = data.citations.find(function(c) {
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