/* 1671번
 * 상어의 저녁식사
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Stack;


class Shark {
    long size;
    long speed;
    long intelligence;

    boolean canEat(Shark prey) {
        return (this.size >= prey.size
                && this.speed >= prey.speed
                && this.intelligence >= prey.intelligence);
    }

    boolean isEqual(Shark shark) {
        return (this.size == shark.size
                && this.speed == shark.speed
                && this.intelligence == shark.intelligence);
    }
}


class Node {
    Node parentNode = null;
    Stack<Node> connectedNodes = new Stack<>();
    boolean isMatched = false;
}


public class Main {
    static final int MAX_NUMBER_OF_NODES = 50;
    static final int MATCHINGS_PER_NODE = 2;

    static int numberOfNodes;
    static Node[] nodes;


    public static void main(String[] args) throws IOException {
        setup();
        int answer = maximumBipartiteMatching();
        System.out.println(answer);
    }

    static void setup() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        setupNumberOfNodes(bufferedReader);
        setupNodes(bufferedReader);
    }


    static void setupNumberOfNodes(BufferedReader bufferedReader) throws IOException {
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

        numberOfNodes = Integer.parseInt(stringTokenizer.nextToken());
    }

    static void setupNodes(BufferedReader bufferedReader) throws IOException {
        Shark[] sharks = new Shark[numberOfNodes];
        nodes = new Node[numberOfNodes];

        for (int i = 0; i < numberOfNodes; i++) {
            StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());

            sharks[i] = new Shark();
            sharks[i].size = Long.parseLong(stringTokenizer.nextToken());
            sharks[i].speed = Long.parseLong(stringTokenizer.nextToken());
            sharks[i].intelligence = Long.parseLong(stringTokenizer.nextToken());

            nodes[i] = new Node();
            for (int j = 0; j < i; j++) {
                if (sharks[i].canEat(sharks[j])) {
                    nodes[i].connectedNodes.push(nodes[j]);
                }
                if (sharks[j].canEat(sharks[i]) && !sharks[j].isEqual(sharks[i])) {
                    nodes[j].connectedNodes.push(nodes[i]);
                }
            }
        }
    }

    static boolean matchingUsingDFS(Node node) {
        for (Node childNode : node.connectedNodes) {
            if (childNode.isMatched)
                continue;

            childNode.isMatched = true;
            if (childNode.parentNode == null || matchingUsingDFS(childNode.parentNode)) {
                childNode.parentNode = node;
                return true;
            }
        }
        return false;
    }

    static int maximumBipartiteMatching() {
        int numberOfRootNodes = 0;

        for (int i = 0; i < numberOfNodes; i++) {
            for (int j = 0; j < MATCHINGS_PER_NODE; j++) {
                clearMatchings();
                matchingUsingDFS(nodes[i]);
            }
        }

        for (int i = 0; i < numberOfNodes; i++) {
            if (nodes[i].parentNode == null)
                numberOfRootNodes++;
        }
        return numberOfRootNodes;
    }

    static void clearMatchings() {
        for (int i = 0; i < numberOfNodes; i++) {
            nodes[i].isMatched = false;
        }
    }
}
