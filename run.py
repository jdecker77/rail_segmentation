#!/Users/jessedecker/miniconda3/envs/tf/bin/python

from PPE import ppe
import os

# start server
port = int(os.environ.get('PORT', 8099))
ppe.run(host='0.0.0.0', port=port)
