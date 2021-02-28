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

func findNodeByID(id int, node *Node) (*Node, bool) {
	if id == node.ID {
		return node, true
	}

	if len(node.Children) > 0 {
		for _, child := range node.Children {
			if node, ok := findNodeByID(id, child); ok {
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
		return errors.New("parent ID shouldn't be higher than this ID")
	}

	if record.Parent == record.ID {
		return errors.New("ID's of parent and Node can't be equal")
	}

	// Does this already exist?
	if _, ok := findNodeByID(record.ID, rootNode); ok {
		return errors.New("already exists")
	}

	return nil
}

// Build takes records and returns the root node of a tree representation
func Build(records []Record) (*Node, error) {
	if len(records) == 0 {
		return nil, nil
	}

	sort.SliceStable(records, func(i, j int) bool {
		return records[i].ID < records[j].ID
	})

	var rootNode *Node
	for idx, r := range records {
		if idx == 0 {
			if r.ID >= 1 || r.Parent >= 1 {
				return nil, errors.New("root can't have parent")
			}
			rootNode = &Node{
				ID: r.ID,
			}
			continue
		}

		if idx < r.ID {
			return nil, errors.New("Non-continuous node")
		}

		if err := validateRecord(r, rootNode); err != nil {
			return nil, err
		}

		if node, ok := findNodeByID(r.Parent, rootNode); ok {
			node.appendChild(&Node{
				ID: r.ID,
			})
		}
	}

	return rootNode, nil
}
