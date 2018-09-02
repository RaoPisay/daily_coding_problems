package com.twitter;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

class TrieNode {
	char data;
	LinkedList<TrieNode> children;
	TrieNode parent;
	boolean isEnd;

	public TrieNode(char data) {
		this.data = data;
		this.children = new LinkedList<TrieNode>();
	}

	public TrieNode getChild(char data) {
		TrieNode child = null;
		for (TrieNode eachChild : this.children) {
			if (eachChild.data == data) {
				child = eachChild;
				break;
			}
		}
		return child;
	}

	public List<String> getWords() {
		List<String> words = new ArrayList<String>();
		if (isEnd) {
			words.add(toString());
		}
		if (this.children != null) {
			for (TrieNode eachChild : children) {
				words.addAll(eachChild.getWords());
			}
		}
		return words;
	}

	public String toString() {
		if (this.parent == null) {
			return "";
		}
		return this.parent.toString() + new String(data + "");
	}
}

class Trie {
	TrieNode root;

	public Trie() {
		root = new TrieNode(' ');
	}

	public void insert(String word) {
		if (search(word)) {
			return;
		}

		TrieNode current = root;
		TrieNode pre = root;
		for (char c : word.toCharArray()) {
			TrieNode child = current.getChild(c);
			if (child != null) {
				current = child;
				child.parent = pre;
				pre = current;
			} else {
				current.children.add(new TrieNode(c));
				current = current.getChild(c);
				current.parent = pre;
				pre = current;
			}
		}
		current.isEnd = true;
	}

	public boolean search(String word) {
		boolean isWordExists = false;
		TrieNode current = this.root;
		for (char c : word.toCharArray()) {
			if (current.getChild(c) == null) {
				return false;
			}
			current = current.getChild(c);
		}

		if (current.isEnd) {
			isWordExists = true;
		}
		return isWordExists;
	}

	public List<String> autcomplete(String prefix) {
		List<String> words = new ArrayList<String>();
		TrieNode lastNode = root;
		for (char c : prefix.toCharArray()) {
			lastNode = lastNode.getChild(c);
			if (lastNode == null) {
				break;
			}
		}
		if (lastNode != null) {
			words.addAll(lastNode.getWords());
		}
		return words;
	}
}

public class AutoCompleteSystem {

	public static void main(String[] args) {
		Trie trie = new Trie();
		trie.insert("Amazing");
		trie.insert("Amazon");
		trie.insert("Amazing Zing Zing");
		trie.insert("Bat");
		trie.insert("Bath");
		trie.insert("Bathing");
		List<String> words = trie.autcomplete("Bat");
		System.out.println(Arrays.toString(words.toArray()));
		words = trie.autcomplete("Ama");
		System.out.println(Arrays.toString(words.toArray()));
	}
}