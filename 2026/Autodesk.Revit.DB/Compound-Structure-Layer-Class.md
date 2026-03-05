# Compound Structure Layer Class

Source: https://www.revitapidocs.com/2026/faece83a-6d49-41b0-2713-fe6cfaa5a3b5.htm

---

| Compound Structure Layer Class |
| --- |

Describes a single layer in a CompoundStructure. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB CompoundStructureLayer 
  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class CompoundStructureLayer : IDisposable
```

```
Public Class CompoundStructureLayer
	Implements IDisposable
```

```
public ref class CompoundStructureLayer : IDisposable
```

```
type CompoundStructureLayer = 
    class
        interface IDisposable
    end
```
The CompoundStructureLayer type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Constructors 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CompoundStructureLayer](4f96e798-f9f3-f4bc-400a-144aca23d844.htm) | Creates a compound structure layer using default settings. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CompoundStructureLayer(CompoundStructureLayer)](6ed93e8c-9045-9099-44f7-4a92fc61ffa7.htm) | Creates a copy of a compound structure layer. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [CompoundStructureLayer(Double, MaterialFunctionAssignment, ElementId)](Compound-Structure-Layer-Double-Material-Function-Assignment-Element-Id-Constructor.md) | Creates a default compound structure layer based on the given width, function and material element id. The priority is initialized with 999\. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DeckEmbeddingType](a42d8678-ec33-faef-de00-371c5bda10c9.htm) | Embedding type for structural deck \- only for a layer whose function is StructuralDeck. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DeckProfileId](7bd864e9-3e9d-f4dd-ddf7-57e70ce8c8ba.htm) | The ElementId of the structural deck profile \- only for a layer whose function is StructuralDeck. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Function](7b4a274c-2ff0-2ecc-5e3b-ab1d46f3d268.htm) | The function of the layer. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](90612f1e-66d2-9b7f-5f69-9306e04e3cc6.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [LayerCapFlag](692333a8-4879-bec3-cb25-9eece96a1bea.htm) | Identifies if the layer participates in wrapping at end caps and/or inserts. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [LayerId](7b6ace8a-7810-5e6d-760e-642361fbe916.htm) | The id of the layer \- note that this may be different from the index in the array of layers in a CompoundStructure. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [LayerPriority](Compound-Structure-Layer-Layer-Priority-Property.md) | The priority of the layer. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [MaterialId](c5a502aa-217c-b76b-b1ad-33f57cc7b24d.htm) | Id of the material assigned to this layer. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Width](0889be74-8b9c-b498-54c1-04d41db3f6ce.htm) | Width of the layer. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](6d5fe33c-dce4-1a69-d27e-c5472cf8363e.htm) | Releases all resources used by the CompoundStructureLayer |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
