# XML Processing

## Overview

- **What is it?** XML processing parses and builds hierarchical tagged documents.
- **Why is it important?** Enterprise systems, SOAP, RSS, and config still use XML.
- **Where is it used?** Legacy integrations, Android layouts, publishing pipelines.

## Learning Objectives

- **Skills gained:** Practical command of XML Processing.
- **Concepts covered:**

- Parse XML with ElementTree.
- Navigate elements and attributes.
- Build XML safely.

- **Expected outcome:** You read and produce XML without fragile string concat.

## Real World Applications

- Telecom
- Publishing
- Government
- Enterprise ERP

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### ElementTree

- **Definition:** Parse XML to tree.
- **Visual explanation:** `ElementTree` → process → result
- **Practical example:**

```python
import xml.etree.ElementTree as ET
root = ET.fromstring('<item id="1">A</item>')
print(root.tag, root.attrib)
```

### find/findall

- **Definition:** Query child elements.
- **Visual explanation:** `find/findall` → process → result
- **Practical example:**

```python
import xml.etree.ElementTree as ET
root = ET.fromstring('<root><a/><b/></root>')
print(len(root.findall('.')))
```

### tostring

- **Definition:** Serialize element.
- **Visual explanation:** `tostring` → process → result
- **Practical example:**

```python
import xml.etree.ElementTree as ET
e = ET.Element('note')
print(ET.tostring(e, encoding='unicode')[:5])
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | XML is a tree of tagged nodes with attributes. |
| ⚡ Purpose | Structured document interchange. |
| 🔥 Benefits | Schema validation (XSD), namespaces, mature tooling. |
| 🎯 Use Cases | RSS feeds, SOAP envelopes, config files. |
| 🚀 Best Practices | Use ElementTree; avoid XML external entities; validate schema. |
| ❌ Common Mistakes | String templating XML, billion laughs, no namespaces handling. |

## Syntax Guide

### Basic Syntax

```python
import xml.etree.ElementTree as ET
ET.parse('file.xml')
```

### Standard Structure

```python
parse -> traverse -> mutate -> write
```

### Code Pattern

```python
for child in root.findall('record'):
    process(child)
```

## Examples

### Beginner Example

```python
import xml.etree.ElementTree as ET

xml = '<catalog><book id="bk1"/></catalog>'
root = ET.fromstring(xml)
print(root[0].tag)
```

### Intermediate Example

```python
import xml.etree.ElementTree as ET

data = '''<users><user name="Ada"/><user name="Lin"/></users>'''
names = [u.attrib['name'] for u in ET.fromstring(data).findall('user')]
print(names)
```

### Advanced Example

```python
import xml.etree.ElementTree as ET


def build_order(order_id: str, sku: str) -> str:
    root = ET.Element('order', id=order_id)
    item = ET.SubElement(root, 'item', sku=sku)
    item.text = '1'
    return ET.tostring(root, encoding='unicode')


print(build_order('100', 'ABC')[:20])
```

## Workflow Diagram

```mermaid
flowchart LR
    A[XML Text] --> B[Parser]
    B --> C[Element Tree]
```

---
