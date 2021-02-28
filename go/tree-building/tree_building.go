package tree

import (
	"errors"
	"sort"
)

// Record represents a record
type Record struct {
	ID     int
	Parent int
}

// Node represents a node in a tree structure
type Node struct {
	ID       int
	Children []*Node
}

func (n *Node) appendChild(node *Node) {
	n.Children = append(n.Children, node)
	n.sortChildren()
}

func (n *Node) sortChildren() {
	sort.SliceStable(n.Children, func(i, j int) bool {
		return n.Children[i].ID < n.Children[j].ID
	})
}

func buildRootNode(r Record) (*Node, error) {
	if r.ID >= 1 || r.Parent >= 1 {
		return nil, errors.New("root can't have parent")
	}
	return &Node{ID: 0}, nil
}

func findNodeByID(id int, node *Node) (*Node, bool) {
	if id == node.ID {
		return node, true
	}

	if len(node.Children) > 0 {
		for _, child := range node.Children {
			if node, found := findNodeByID(id, child); found {
				return node, true
			}
		}
	}
	return nil, false
}

func validateRecord(record Record, rootNode *Node) error {
	if record.ID == rootNode.ID && record.Parent >= 1 {
		return errors.New("root node can't have parent")
	}

	if record.ID == rootNode.ID {
		return errors.New("can't have multiple roots")
	}

	if record.Parent > record.ID {
		return errors.New("parent ID shouldn't be higher than child ID")
	}

	if record.Parent == record.ID {
		return errors.New("ID's of parent and Node can't be equal")
	}

	if _, found := findNodeByID(record.ID, rootNode); found {
		return errors.New("node already exists")
	}

	return nil
}

// Build takes records and returns the root node of the tree representation
func Build(records []Record) (*Node, error) {
	if len(records) == 0 {
		return nil, nil
	}

	sort.SliceStable(records, func(i, j int) bool {
		return records[i].ID < records[j].ID
	})

	var rootNode *Node
	for index, r := range records {
		if index < r.ID {
			return nil, errors.New("Non-continuous node, can't build tree")
		}

		if index == 0 {
			if node, err := buildRootNode(r); err == nil {
				rootNode = node
			} else {
				return nil, err
			}
			continue
		}

		if err := validateRecord(r, rootNode); err != nil {
			return nil, err
		}

		if node, found := findNodeByID(r.Parent, rootNode); found {
			node.appendChild(&Node{ID: r.ID})
		}
	}

	return rootNode, nil
}
