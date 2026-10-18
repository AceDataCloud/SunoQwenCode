import json
from pathlib import Path
import unittest
from urllib.parse import parse_qs, urlparse
import re

ROOT = Path(__file__).resolve().parents[1]

class ManifestTests(unittest.TestCase):
    def test_native_secret_and_service_isolation(self):
        data = json.loads((ROOT / 'qwen-extension.json').read_text())
        self.assertEqual(len(data['mcpServers']), 1)
        self.assertEqual(len(data['settings']), 1)
        secret = data['settings'][0]
        self.assertTrue(secret['sensitive'])
        server = next(iter(data['mcpServers'].values()))
        self.assertEqual(server['headers']['Authorization'], 'Bearer $' + secret['envVar'])
        self.assertTrue(server['httpUrl'].startswith('https://'))
        self.assertNotIn('trust', server)
        self.assertTrue(server['includeTools'])
        self.assertNotIn('hooks', data)
        self.assertNotIn('workflows', data)

    def test_onboarding_links_and_artifacts(self):
        for filename in ['README.md', 'readme/README_zh_Hans.md']:
            content = (ROOT / filename).read_text()
            self.assertIn('General application', content)
            self.assertIn('task_id', content)
            for url in re.findall(r'https://platform[.]acedata[.]cloud[^)\s]+', content):
                query = parse_qs(urlparse(url).query)
                self.assertEqual(set(query), {'utm_source','utm_medium','utm_campaign','utm_content'})
                self.assertEqual(query['utm_source'], ['github'])
            for image in re.findall(r'!\[[^]]*\]\(([^)]+)\)', content):
                self.assertTrue((ROOT / filename).parent.joinpath(image).resolve().is_file(), image)

if __name__ == '__main__':
    unittest.main()
